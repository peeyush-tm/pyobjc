#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import sys
import os
import glob
import site

def globall(*args):
    res = []
    for arg in args:
        res.extend(glob.glob(arg))
    return res

# If true we'll build universal binaries on systems with the 10.4u SDK running
# OS X 10.4 or later.
# 
# NOTE: This is an experimental feature.
AUTO_UNIVERSAL = 0

# Add our utility library to the path
site.addsitedir(os.path.abspath('source-deps'))
sys.path.insert(1,
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'setup-lib')))

from pyobjc_commands import extra_cmdclass
from if_framework import IfFramework, CFLAGS, ALL_LDFLAGS, LDFLAGS, frameworks

# Some PiPy stuff
LONG_DESCRIPTION="""
PyObjC is a bridge between Python and Objective-C.  It allows full
featured Cocoa applications to be written in pure Python.  It is also
easy to use other frameworks containing Objective-C class libraries
from Python and to mix in Objective-C, C and C++ source.

Python is a highly dynamic programming language with a shallow learning
curve.  It combines remarkable power with very clear syntax.

The installer package installs a number of Xcode templates for
easily creating new Cocoa-Python projects.

PyObjC also supports full introspection of Objective-C classes and
direct invocation of Objective-C APIs from the interactive interpreter.

PyObjC requires MacOS X 10.2 or later.  PyObjC works both with the Apple
provided Python installation in MacOS X 10.2 (and later) and with
MacPython 2.3.  Users of MacPython 2.3 can install PyObjC though the
PackageManager application.
"""

from setuptools import setup, Extension
import os

FFI_CFLAGS=['-Ilibffi-src/include']

# The list below includes the source files for all CPU types that we run on
# this makes it easier to build fat binaries on Mac OS X.
FFI_SOURCE=[
    "libffi-src/src/types.c",
    "libffi-src/src/prep_cif.c",
    "libffi-src/src/x86/ffi_darwin.c",
    "libffi-src/src/x86/darwin.S",
    "libffi-src/src/powerpc/ffi_darwin.c",
    "libffi-src/src/powerpc/darwin.S",
    "libffi-src/src/powerpc/darwin_closure.S",
]

# Patch distutils: it needs to compile .S files as well.
from distutils.unixccompiler import UnixCCompiler
UnixCCompiler.src_extensions.append('.S')
del UnixCCompiler

def flags(name):
    return ALL_LDFLAGS.get(name, [])

CorePackages = ['objc']
objcExtension = Extension("objc._objc",
    FFI_SOURCE + glob.glob(os.path.join('Modules', 'objc', '*.m')),
    extra_compile_args=CFLAGS + FFI_CFLAGS,
    extra_link_args=flags('objc') + LDFLAGS,
)

CoreExtensions =  [objcExtension]

for test_source in glob.glob(os.path.join('Modules', 'objc', 'test', '*.m')):
    name, ext = os.path.splitext(os.path.basename(test_source))

    if name != 'ctests':
        ext = Extension('objc.test.' + name,
            [test_source],
            extra_compile_args=['-IModules/objc'] + CFLAGS,
            extra_link_args=flags('objc'))
    else:
        ext = Extension('objc.test.' + name,
            [test_source] + FFI_SOURCE,
            extra_compile_args=['-IModules/objc'] + CFLAGS + FFI_CFLAGS,
            extra_link_args=flags('objc') + LDFLAGS)

    CoreExtensions.append(ext)

INCFILES = glob.glob('build/codegen/*.inc')
DEPENDS = dict(
    CoreFoundation=[],
    Foundation=globall('build/codegen/_Fnd_*.inc', 'Modules/Foundation/*.m'),
    AppKit=globall('build/codegen/_App_*.inc', 'Modules/AppKit/*.m'),
    AddressBook=INCFILES,
    SecurityInterface=INCFILES,
    ExceptionHandling=INCFILES,
    PrefPanes=INCFILES,
    InterfaceBuilder=INCFILES,
    WebKit=INCFILES,
    AppleScriptKit=INCFILES,
    Automator=INCFILES,
    CoreData=INCFILES,
    DiscRecording=INCFILES,
    DiscRecordingUI=INCFILES,
    SyncServices=INCFILES,
    XgridFoundation=INCFILES,
    QTKit=INCFILES,
    Quartz=INCFILES,
    OSAKit=INCFILES,
    SenTestingKit=INCFILES,
)

def deps(name):
    incs = DEPENDS.get(name, [])
    if not incs:
        return {}
    return dict(depends=incs)
    
PACKAGES = {}
def pkg(name, *extras, **options):
    extensions = []
    f = flags(name)
    if not f:
        f = frameworks(name, 'Foundation')
    if not options.get('no_extension'):
        extensions.append(Extension(
            name + '._' + name,
            ['Modules/%s/_%s.m' % (name, name)],
            extra_compile_args=['-IModules/objc'] + CFLAGS,
            extra_link_args=f + LDFLAGS,
            **deps(name)))
    extensions.extend(extras)

    if options.get('no_package'):
        p = []
    else:
        p = [name]
    packages, extensions = IfFramework(name + '.framework', p, extensions)
    PACKAGES[name] = packages, extensions

pkg('CoreFoundation',
    Extension("PyObjCTools._machsignals",
        ['Modules/CoreFoundation/machsignals.m'],
        extra_compile_args=['-IModules/objc'] + CFLAGS,
        extra_link_args=flags('CoreFoundation') + LDFLAGS,
        **deps('CoreFoundation')
    ),
    no_extension=True,
    no_package=True,
)


pkg('Foundation')
pkg('AppKit')
pkg('AddressBook')
pkg('SecurityInterface')
pkg('ExceptionHandling')
pkg('PreferencePanes')
pkg('ScreenSaver', no_extension=True)
pkg('Message', no_extension=True)
pkg('InterfaceBuilder')
pkg('SenTestingKit')
pkg('WebKit')
pkg('XgridFoundation')
pkg('CoreData')
pkg('DiscRecording')
pkg('DiscRecordingUI')
pkg('SyncServices')
pkg('Automator')
pkg('QTKit')
pkg('Quartz')
pkg('OSAKit')
pkg('AppleScriptKit')

def package_version():
    fp = open('Modules/objc/pyobjc.h', 'r')
    for ln in fp.readlines():
        if ln.startswith('#define OBJC_VERSION'):
            fp.close()
            return ln.split()[-1][1:-1]

    raise ValueError, "Version not found"

packages = ['PyObjCTools', 'PyObjCTools.XcodeSupport'] + CorePackages
extensions = [] + CoreExtensions
for name, (pkgs, exts) in PACKAGES.iteritems():
    packages.extend(pkgs)
    extensions.extend(exts)

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, 'Lib/' + pkg.replace('.', '/')) for pkg in packages])

for aPackage in package_dir.keys():
    testDir = os.path.join(package_dir[aPackage], 'test')
    if os.path.isdir(testDir):
        packageName = '%s.test' % aPackage
        package_dir[packageName] = testDir
        packages.append(packageName)

package_dir[''] = 'Lib'

CLASSIFIERS = filter(None,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Environment :: MacOS X :: Cocoa
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: MacOS :: MacOS X
Programming Language :: Python
Programming Language :: Objective C
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: User Interfaces
""".splitlines())

dist = setup(
    name="pyobjc",
    version=package_version(),
    description="Python<->ObjC Interoperability Module",
    long_description=LONG_DESCRIPTION,
    author="bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email="pyobjc-dev@lists.sourceforge.net",
    url="http://pyobjc.sourceforge.net/",
    platforms=['MacOS X'],
    ext_modules=extensions,
    packages=packages,
    package_dir=package_dir,
    cmdclass=extra_cmdclass,
    classifiers=CLASSIFIERS,
    license='MIT License',
    download_url='http://pyobjc.sourceforge.net/software/index.php',
    setup_requires=[
        "py2app>=0.3.dev-r610,==dev",
        "bdist_mpkg>=0.3,==dev",
    ],
    extras_require={
        'XcodeSupport': [
            "py2app>=0.3.dev-r610,==dev",
            "altgraph>=0.6.6,==dev",
        ],
    },
    entry_points={
        'console_scripts': [
            "nibclassbuilder = PyObjCTools.NibClassBuilder:commandline",
        ],
    },
    zip_safe=False,
)

if 'install' in sys.argv:
    import textwrap
    print textwrap.dedent(
    """
    **NOTE**

    Installing PyObjC with "setup.py install" *does not* install the following:
    
    - py2app (bdist_mpkg, modulegraph, altgraph, ...) and its tools
    - Xcode templates
    - Documentation
    - Example code

    The recommended method for installing PyObjC is to do:
        
        $ python setup.py bdist_mpkg --open

    This will create and open an Installer metapackage that contains PyObjC,
    py2app, and all the goodies!
    """)
