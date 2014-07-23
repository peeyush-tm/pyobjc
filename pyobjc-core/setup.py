import sys
import subprocess
import shutil
import re
import os
import plistlib
import glob
import site
import platform

try:
    import setuptools

except ImportError:
    # setuptools is required to run the setup file, bail out early
    print("This package requires setuptools to build")
    sys.exit(1)


from pkg_resources import working_set, normalize_path, add_activation_listener, require

from setuptools import setup, Extension, find_packages
from distutils import log
from distutils.core import Command
from distutils.errors import DistutilsPlatformError, DistutilsSetupError, DistutilsError
from setuptools.command import build_py, test, egg_info
from setuptools.command import build_ext, install_lib

# We need at least Python 2.7
MIN_PYTHON = (2, 7)

if sys.version_info < MIN_PYTHON:
    vstr = '.'.join(map(str, MIN_PYTHON))
    raise SystemExit('PyObjC: Need at least Python ' + vstr)

#
#
# Compiler arguments
#
#

# CFLAGS for the objc._objc extension:
CFLAGS = [
    "-DPyObjC_STRICT_DEBUGGING",
    "-DMACOSX", # For libffi
    "-DPyObjC_BUILD_RELEASE=%02d%02d"%(
        tuple(map(int, platform.mac_ver()[0].split('.')[:2]))),
    "-DMACOSX",
    "-g",
    "-fexceptions",

    # Loads of warning flags
    "-Wall", "-Wstrict-prototypes", "-Wmissing-prototypes",
    "-Wformat=2", "-W",
    "-Wpointer-arith",
    "-Wmissing-declarations",
    "-Wnested-externs",
    "-W",
    "-Wno-import",
    "-Wno-unknown-pragmas",
    #"-fvisibility=protected",
    "-Wshorten-64-to-32",
    #"-Werror",
]

# CFLAGS for other (test) extensions:
EXT_CFLAGS = CFLAGS + ["-IModules/objc"]

# LDFLAGS for the objc._objc extension
OBJC_LDFLAGS = [
    '-framework', 'CoreFoundation',
    '-framework', 'Foundation',
    '-framework', 'Carbon',
    '-fvisibility=protected',
    '-g', '-O1', # XXX
]


#
#
# Adjust distutils CFLAGS:
#
# - PyObjC won't work when compiled with -O0
# - To make it easier to debug reduce optimization level
#   to -O1 when building with a --with-pydebug build of Python
# - Set optimization to -O4 with normal builds of Python,
#   enables link-time optimization with clang and appears to
#   be (slightly) faster.
#

from distutils.sysconfig import get_config_var, get_config_vars

if '-O0' in get_config_var('CFLAGS'):
    # -O0 doesn't work with some (older?) compilers, unconditionally
    # change -O0 to -O1 to work around that issue.
    print ("Change -O0 to -O1 (-O0 miscompiles libffi)")
    vars = get_config_vars()
    for k in vars:
        if isinstance(vars[k], str) and '-O0' in vars[k]:
            vars[k] = vars[k].replace('-O0', '-O1')


if get_config_var('Py_DEBUG'):
    # Running with Py_DEBUG, reduce optimization level
    # to make it easier to debug the code.
    cfg_vars = get_config_vars()
    for k in vars:
        if isinstance(cfg_vars[k], str) and '-O2' in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace('-O2', '-O1 -g')
        elif isinstance(cfg_vars[k], str) and '-O3' in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace('-O3', '-O1 -g')

else:
    # Enable -O4, which enables link-time optimization with
    # clang. This appears to have a positive effect on performance.
    cfg_vars = get_config_vars()
    for k in cfg_vars:
        if isinstance(cfg_vars[k], str) and '-O2' in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace('-O2', '-O3')
        elif isinstance(cfg_vars[k], str) and '-O3' in cfg_vars[k]:
            cfg_vars[k] = cfg_vars[k].replace('-O3', '-O3')


# XXX: bug in CPython 3.4 repository leaks unwanted compiler flag into disutils.
cfg_vars = get_config_vars()
for k in cfg_vars:
    if isinstance(cfg_vars[k], str) and '-Werror=declaration-after-statement' in cfg_vars[k]:
        cfg_vars[k] = cfg_vars[k].replace('-Werror=declaration-after-statement', '')





#
# Support for an embedded copy of libffi
#
FFI_CFLAGS=['-Ilibffi-src/include', '-Ilibffi-src/powerpc']

# The list below includes the source files for all CPU types that we run on
# this makes it easier to build fat binaries on Mac OS X.
FFI_SOURCE=[
    "libffi-src/ffi.c",
    "libffi-src/types.c",
    "libffi-src/powerpc/ppc-darwin.S",
    "libffi-src/powerpc/ppc-darwin_closure.S",
    "libffi-src/powerpc/ppc-ffi_darwin.c",
    "libffi-src/powerpc/ppc64-darwin_closure.S",
    "libffi-src/x86/darwin64.S",
    "libffi-src/x86/x86-darwin.S",
    "libffi-src/x86/x86-ffi64.c",
    "libffi-src/x86/x86-ffi_darwin.c",
]




# Patch distutils: it needs to compile .S files as well.
from distutils.unixccompiler import UnixCCompiler
UnixCCompiler.src_extensions.append('.S')
del UnixCCompiler


#
#
# Custom distutils commands
#
#

def verify_platform():
    if sys.platform != 'darwin':
        raise DistutilsPlatformError("PyObjC requires Mac OS X to build")

    if sys.version_info[:2] < (2, 7):
        raise DistutilsPlatformError("PyObjC requires Python 2.7 or later to build")


class oc_build_py (build_py.build_py):
    def run(self):
        verify_platform()
        build_py.build_py.run(self)

    def build_packages(self):
        log.info("Overriding build_packages to copy PyObjCTest")
        p = self.packages
        self.packages = list(self.packages) + ['PyObjCTest']
        try:
            build_py.build_py.build_packages(self)
        finally:
            self.packages = p


class oc_test (test.test):
    description = "run test suite"
    user_options = [
        ('verbosity=', None, "print what tests are run"),
    ]

    def initialize_options(self):
        self.verbosity='1'

    def finalize_options(self):
        if isinstance(self.verbosity, str):
            self.verbosity = int(self.verbosity)


    def cleanup_environment(self):
        ei_cmd = self.get_finalized_command('egg_info')
        egg_name = ei_cmd.egg_name.replace('-', '_')

        to_remove =  []
        for dirname in sys.path:
            bn = os.path.basename(dirname)
            if bn.startswith(egg_name + "-"):
                to_remove.append(dirname)

        for dirname in to_remove:
            log.info("removing installed %r from sys.path before testing"%(
                dirname,))
            sys.path.remove(dirname)

        from pkg_resources import add_activation_listener
        add_activation_listener(lambda dist: dist.activate())
        working_set.__init__()

    def add_project_to_sys_path(self):
        from pkg_resources import normalize_path, add_activation_listener
        from pkg_resources import working_set, require

        if getattr(self.distribution, 'use_2to3', False):

            # Using 2to3, cannot do this inplace:
            self.reinitialize_command('build_py', inplace=0)
            self.run_command('build_py')
            bpy_cmd = self.get_finalized_command("build_py")
            build_path = normalize_path(bpy_cmd.build_lib)

            self.reinitialize_command('egg_info', egg_base=build_path)
            self.run_command('egg_info')

            self.reinitialize_command('build_ext', inplace=0)
            self.run_command('build_ext')

        else:
            self.reinitialize_command('egg_info')
            self.run_command('egg_info')
            self.reinitialize_command('build_ext', inplace=1)
            self.run_command('build_ext')

        self.__old_path = sys.path[:]
        self.__old_modules = sys.modules.copy()

        if 'PyObjCTools' in sys.modules:
            del sys.modules['PyObjCTools']

        ei_cmd = self.get_finalized_command('egg_info')
        sys.path.insert(0, normalize_path(ei_cmd.egg_base))
        sys.path.insert(1, os.path.dirname(__file__))

        add_activation_listener(lambda dist: dist.activate())
        working_set.__init__()
        require('%s==%s'%(ei_cmd.egg_name, ei_cmd.egg_version))

    def remove_from_sys_path(self):
        from pkg_resources import working_set
        sys.path[:] = self.__old_path
        sys.modules.clear()
        sys.modules.update(self.__old_modules)
        working_set.__init__()


    def run(self):
        verify_platform()

        be_cmd = self.get_finalized_command('build_ext')

        import unittest

        # Ensure that build directory is on sys.path (py3k)
        import sys

        self.cleanup_environment()
        self.add_project_to_sys_path()

        from PyObjCTest.loader import makeTestSuite
        import PyObjCTools.TestSupport as mod

        try:
            meta = self.distribution.metadata
            name = meta.get_name()
            test_pkg = name + "_tests"
            suite = makeTestSuite(be_cmd.use_system_libffi)

            runner = unittest.TextTestRunner(verbosity=self.verbosity)
            result = runner.run(suite)

            # Print out summary. This is a structured format that
            # should make it easy to use this information in scripts.
            summary = dict(
                count=result.testsRun,
                fails=len(result.failures),
                errors=len(result.errors),
                xfails=len(getattr(result, 'expectedFailures', [])),
                xpass=len(getattr(result, 'expectedSuccesses', [])),
                skip=len(getattr(result, 'skipped', [])),
            )
            print("SUMMARY: %s"%(summary,))

            if not result.wasSuccessful():
                raise DistutilsError("some tests failed")

        finally:
            self.remove_from_sys_path()


class oc_egg_info (egg_info.egg_info):
    # This is a workaround for a bug in setuptools: I'd like
    # to use the 'egg_info.writers' entry points in the setup()
    # call, but those don't work when also using a package_base
    # argument as we do.
    # (issue 123 in the distribute tracker)
    def run(self):
        verify_platform()

        self.mkpath(self.egg_info)

        for hdr in ("pyobjc-compat.h", "pyobjc-api.h"):
            fn = os.path.join("include", hdr)

            self.write_header(fn, os.path.join(self.egg_info, fn))

        egg_info.egg_info.run(self)

    def write_header(self, basename, filename):
        with open(os.path.join('Modules/objc/', os.path.basename(basename)), 'rU') as fp:
            data = fp.read()
        if not self.dry_run:
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))

        self.write_file(basename, filename, data)



class oc_install_lib (install_lib.install_lib):
    def run(self):
        verify_platform()
        install_lib.install_lib.run(self)

    def get_exclusions(self):
        result = install_lib.install_lib.get_exclusions(self)
        if hasattr(install_lib, '_install_lib'):
            outputs = install_lib._install_lib.get_outputs(self)
        else:
            outputs = install_lib.orig.install_lib.get_outputs(self)

        for fn in outputs:
            if 'PyObjCTest' in fn:
                result[fn] = 1

        for fn in os.listdir('PyObjCTest'):
            result[os.path.join('PyObjCTest', fn)] = 1
            result[os.path.join(self.install_dir, 'PyObjCTest', fn)] = 1


        return result


def _find_executable(executable):
    if os.path.isfile(executable):
        return executable

    else:
        for p in os.environ['PATH'].split(os.pathsep):
            f = os.path.join(p, executable)
            if os.path.isfile(f):
                return executable
    return None

def _working_compiler(executable):
    import tempfile, subprocess, shlex
    with tempfile.NamedTemporaryFile(mode='w', suffix='.c') as fp:
        fp.write('#include <stdarg.h>\nint main(void) { return 0; }\n')
        fp.flush()

        cflags = get_config_var('CFLAGS')
        cflags = shlex.split(cflags)
        cflags += CFLAGS

        p = subprocess.Popen([
            executable, '-c', fp.name] + cflags,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        exit = p.wait()
        if exit != 0:
            return False

        binfile = fp.name[:-1] + 'o'
        if os.path.exists(binfile):
            os.unlink(binfile)

        binfile = os.path.basename(binfile)
        if os.path.exists(binfile):
            os.unlink(binfile)

    return True

def _fixup_compiler():
    if 'CC' in os.environ:
        # CC is in the environment, always use explicit
        # overrides.
        return

    cc = oldcc = get_config_var('CC').split()[0]
    cc = _find_executable(cc)
    if cc is not None and os.path.basename(cc).startswith('gcc'):
        # Check if compiler is LLVM-GCC, that's known to
        # generate bad code.
        data = os.popen("'%s' --version 2>/dev/null"%(
            cc.replace("'", "'\"'\"'"),)).read()
        if 'llvm-gcc' in data:
            cc = None

    if cc is not None and not _working_compiler(cc):
        cc = None

    if cc is None:
        # Default compiler is not useable, try finding 'clang'
        cc = _find_executable('clang')
        if cc is None:
            cc = os.popen("/usr/bin/xcrun -find clang").read()

    if not cc:
        raise DistutilsPlatformError("Cannot locate compiler candidate")

    if not _working_compiler(cc):
        raise DistutilsPlatformError("Cannot locate a working compiler")

    if cc != oldcc:
        log.info("Use '%s' instead of '%s' as the compiler"%(cc, oldcc))

        vars = get_config_vars()
        for env in ('BLDSHARED', 'LDSHARED', 'CC', 'CXX'):
            if env in vars and env not in os.environ:
                split = vars[env].split()
                split[0] = cc if env != 'CXX' else cc + '++'
                vars[env] = ' '.join(split)


class oc_build_ext (build_ext.build_ext):
    user_options = [
        ('use-system-libffi=', None, "print what tests are run"),
        ('deployment-target=', None, "deployment target to use"),
        ('sdk-root=', None, "Path to the SDK to use, or 'python'"),
    ]
    boolean_options = [ 'use-system-libffi' ]

    def initialize_options(self):
        build_ext.build_ext.initialize_options(self)
        self.use_system_libffi=False
        self.deployment_target = None
        self.sdk_root = None

    def finalize_options(self):
        build_ext.build_ext.finalize_options(self)

        if self.sdk_root is None:
            if os.path.exists('/usr/bin/xcodebuild'):
                self.sdk_root = subprocess.check_output(
                        ['/usr/bin/xcodebuild', '-version', '-sdk', 'macosx', 'Path'],
                        universal_newlines=True).strip()

            else:
                self.sdk_root = '/'

        if not os.path.exists(self.sdk_root):
            raise DistutilsSetupError("SDK root %r does not exist"%(self.sdk_root,))

        if not os.path.exists(os.path.join(self.sdk_root, 'usr/include/objc/runtime.h')):
            if '-DNO_OBJC2_RUNTIME' not in CFLAGS:
                CFLAGS.append('-DNO_OBJC2_RUNTIME')
                EXT_CFLAGS.append('-DNO_OBJC2_RUNTIME')

    def run(self):
        verify_platform()

        if not self.use_system_libffi:
            for ext in self.extensions:
                if ext.name == 'objc._objc':
                    if ext.sources[:-len(FFI_SOURCE)] != FFI_SOURCE:
                        ext.sources.extend(FFI_SOURCE)
                        ext.extra_compile_args.extend(FFI_CFLAGS)

        if self.deployment_target is not None:
            os.environ['MACOSX_DEPLOYMENT_TARGET'] = self.deployment_target

        if self.sdk_root != 'python':
            if '-isysroot' not in CFLAGS:
                CFLAGS.extend(['-isysroot', self.sdk_root])
                EXT_CFLAGS.extend(['-isysroot', self.sdk_root])
                OBJC_LDFLAGS.extend(['-isysroot', self.sdk_root])


        cflags = get_config_var('CFLAGS')
        if '-mno-fused-madd' in cflags:
            cflags = cflags.replace('-mno-fused-madd', '')
            get_config_vars()['CFLAGS'] = cflags

        _fixup_compiler()

        build_ext.build_ext.run(self)
        extensions = self.extensions
        self.extensions = [
                e for e in extensions if e.name.startswith('PyObjCTest') ]
        self.copy_extensions_to_source()
        self.extensions = extensions

#
# Calculate package metadata
#

def parse_package_metadata():
    """
    Read the 'metadata' section of 'setup.cfg' to calculate the package
    metadata (at least those parts that can be configured staticly).
    """
    try:
        from ConfigParser import RawConfigParser
    except ImportError:
        from configparser import RawConfigParser

    cfg = RawConfigParser()
    with open('setup.cfg') as fp:
        cfg.readfp(fp)

    cfg.optionxform = lambda x: x

    metadata = {}
    for opt in cfg.options('metadata'):
        val = cfg.get('metadata', opt)
        if opt in ('classifiers',):
            metadata[opt] = [x for x in val.splitlines() if x]
        elif opt in ('long_description',):
            metadata[opt] = val[1:]
        elif opt in ('packages', 'namespace_packages', 'platforms', 'keywords'):
            metadata[opt] = [x.strip() for x in val.split(',')]

        elif opt in ['zip-safe']:
            metadata['zip_safe'] = int(val)
        else:
            metadata[opt] = val

    metadata['version'] = package_version()

    return metadata

def package_version():
    """
    Return the package version, the canonical location
    for the version is the main header file of the objc._objc
    extension.
    """
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise DistutilsSetupError("Version not found")


#
# Actually call the setup function.
#
# Note that all package metadata is stored in setup.cfg, except those
# bits that require Python code to calculate or are needed to control
# the working of distutils.
#
setup(
    ext_modules = [
        Extension(
            "objc._objc",
            list(glob.glob(os.path.join('Modules', 'objc', '*.m'))),
            extra_compile_args=CFLAGS,
            extra_link_args=OBJC_LDFLAGS,
            depends=list(glob.glob(os.path.join('Modules', 'objc', '*.h'))),
        ),
    ] + [
        Extension(
            "PyObjCTest." + os.path.splitext(os.path.basename(test_source))[0],
            [test_source],
            extra_compile_args=EXT_CFLAGS,
            extra_link_args=OBJC_LDFLAGS)

        for test_source in glob.glob(os.path.join('Modules', 'objc', 'test', '*.m'))
    ],
    cmdclass = {
        'build_ext': oc_build_ext,
        'install_lib': oc_install_lib,
        'build_py': oc_build_py,
        'test': oc_test,
        'egg_info':oc_egg_info
    },
    package_dir = {
        '': 'Lib',
        'PyObjCTest': 'PyObjCTest'
    },
    options = {
        'egg_info': {
            'egg_base': 'Lib'
        }
    },
    **parse_package_metadata()
)
