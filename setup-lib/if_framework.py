import sys, os
import glob
from setuptools import Extension
from srcpath import srcpath, modpath, libpath, buildpath

__all__ = [
    'IfFramework', 'CFLAGS', 'ALL_LDFLAGS', 'LDFLAGS', 'frameworks',
    'PACKAGES', 'pkg', 'deps', 'globall',
    'ldflags', 'DEPENDS', 'INCFILES',
]

# If true we'll build universal binaries on systems with the 10.4u SDK running
# OS X 10.4 or later.
# 
# NOTE: This is an experimental feature.
AUTO_UNIVERSAL = False

# On GNUstep we can read some configuration from the environment.
gs_root = os.environ.get('GNUSTEP_SYSTEM_ROOT')

ALL_LDFLAGS = {}
LDFLAGS = []
PACKAGES = {}
DEPENDS = {}
INCFILES = []

def ldflags(name):
    return ALL_LDFLAGS.get(name, [])

def globall(*args):
    res = []
    for arg in args:
        res.extend(glob.glob(arg))
    return res

def frameworks(*args):
    lst = []
    for arg in args:
        lst.extend(['-framework', arg])
    return lst

def linkswith(name, fmwks=()):
    ALL_LDFLAGS[name] = frameworks(*fmwks)

INCFILES.extend(glob.glob(buildpath('codegen/*.inc')))

DEPENDS.update(dict(
    CoreFoundation=[],
    Foundation=globall(
        buildpath('codegen/_Fnd_*.inc'), modpath('Foundation/*.m')),
    AppKit=globall(buildpath('codegen/_App_*.inc'), modpath('AppKit/*.m')),
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
))

def deps(name):
    incs = DEPENDS.get(name, [])
    if not incs:
        return {}
    return dict(depends=incs)


if gs_root is None:
    #
    # MacOS X
    #
    def IfFramework(name, packages, extensions, headername=None):
        """
        Return the packages and extensions if the framework exists, or
        two empty lists if not.
        """
        for pth in ('/System/Library/Frameworks', '/Library/Frameworks'):
            basedir = os.path.join(pth, name)
            if os.path.exists(basedir):
                if (headername is None) or os.path.exists(
                        os.path.join(basedir, "Headers", headername)):
                    return packages, extensions
        return [], []

    # Double-check
    if sys.platform != 'darwin':
        print "You're not running on MacOS X, and don't use GNUstep"
        print "I don't know how to build PyObjC on such a platform."
        print "Please read the ReadMe."
        print ""
        raise SystemExit("ObjC runtime not found")

    CFLAGS=[
        "-DMACOSX",
        "-DAPPLE_RUNTIME",
        "-no-cpp-precomp",
        "-Wno-long-double",
        "-g",
        #"-O0",

        # Loads of warning flags
        "-Wall", "-Wstrict-prototypes", "-Wmissing-prototypes",
        "-Wformat=2", "-W", "-Wshadow",
        "-Wpointer-arith", #"-Wwrite-strings",
        "-Wmissing-declarations",
        "-Wnested-externs",
        "-Wno-long-long",
        #"-Wfloat-equal",

        # These two are fairly useless:
        #"-Wunreachable-code",
        #"-pedantic",

        "-Wno-import",
        #"-Werror",

        # use the same optimization as Python, probably -O3,
        # but can be overrided by one of the following:

        # no optimization, for debugging
        #"-O0",

        # g4 optimized
        #"-fast", "-fPIC", "-mcpu=7450",

        # g5 optimized
        #"-fast", "-fPIC",
        ]

    linkswith('objc',
        ['Foundation', 'Carbon'])
    linkswith('CoreFoundation',
        ['CoreFoundation', 'Foundation'])
    linkswith('Foundation',
        ['CoreFoundation', 'Foundation'])
    linkswith('AppKit',
        ['CoreFoundation', 'AppKit'])
    linkswith('AddressBook',
        ['CoreFoundation', 'AddressBook', 'Foundation'])
    linkswith('InterfaceBuilder',
        ['CoreFoundation', 'InterfaceBuilder', 'Foundation'])
    linkswith('SecurityInterface',
        ['CoreFoundation', 'SecurityInterface', 'Foundation'])
    linkswith('ExceptionHandling',
        ['CoreFoundation', 'ExceptionHandling', 'Foundation'])
    linkswith('PreferencePanes',
        ['CoreFoundation', 'PreferencePanes', 'Foundation'])
    linkswith('SenTestingKit',
        ['SenTestingKit', 'Foundation'])
    linkswith('WebKit',
        ['WebKit', 'Foundation'])
    linkswith('XgridFoundation',
        ['XgridFoundation', 'Foundation'])

    LDFLAGS = []
    if AUTO_UNIVERSAL:
        if os.path.exists('/Developer/SDKs/MacOSX10.4u.sdk') and int(
                os.uname()[2].split('.')[0]) >= 8:
            CFLAGS.extend([
                    '-arch', 'i386',
                    '-arch', 'ppc',
                    '-isysroot', '/Developer/SDKs/MacOSX10.4u.sdk',
            ])
            LDFLAGS.extend([
                    '-arch', 'i386',
                    '-arch', 'ppc',
                    '-isysroot', '/Developer/SDKs/MacOSX10.4u.sdk',
                    '-Wl,-syslibroot,/Developer/SDKs/MacOSX10.4u.sdk',
            ])


else:
    #
    # GNUstep
    #
    # NOTE: We add '-g' to the compile flags to make development easier
    # on systems where the installed python hasn't been build with debugging
    # support.
    gs_root = gs_root + '/Library'

    LDFLAGS=[]

    gs_cpu = os.environ.get('GNUSTEP_HOST_CPU')
    gs_os = os.environ.get('GNUSTEP_HOST_OS')
    gs_combo = os.environ.get('LIBRARY_COMBO')

    gs_lib_dir = gs_cpu + '/' + gs_os
    gs_flib_dir = gs_cpu + '/' + gs_os + '/' + gs_combo

    def IfFramework(name, packages, extensions, headername=None):
        """
        Return the packages and extensions if the framework exists, or
        two empty lists if not.
        """
        name = os.path.splitext(name)[0]
        for pth in (gs_root,):
            basedir = os.path.join(pth, 'Headers', name)
            if os.path.exists(basedir):
                return packages, extensions
        return [], []

    CFLAGS=[
        '-g',
        ##'-O0',
        '-Wno-import',

        # The flags below should somehow be extracted from the GNUstep
        # build environment (makefiles)!
        '-DGNU_RUNTIME=1',
        '-DGNUSTEP_BASE_LIBRARY=1',
        '-fconstant-string-class=NSConstantString',
        '-fgnu-runtime',
        '-I' + gs_root + '/Headers',
        '-I' + gs_root + '/Headers/gnustep',
        '-I' + gs_root + '/Headers/' + gs_lib_dir
        ]

    ALL_LDFLAGS['objc'] = [
        '-g',
        '-L', gs_root + '/Libraries/',
        '-L', gs_root + '/Libraries/' + gs_flib_dir,
        '-L', gs_root + '/Libraries/' + gs_lib_dir,
        '-lgnustep-base',
        '-lobjc',
    ]

    ALL_LDFLAGS['Foundation'] = ALL_LDFLAGS['objc']
    ALL_LDFLAGS['AppKit'] = ALL_LDFLAGS['objc'] + ['-lgnustep-gui']
    ALL_LDFLAGS['AddressBook'] = ALL_LDFLAGS['objc'] + ['-lAddresses']

CFLAGS.append('-I' + buildpath('codegen/'))

def pkg(name, *extras, **options):
    extensions = []
    f = ldflags(name)
    if not f:
        f = frameworks(name, 'Foundation')
    if not options.get('no_extension'):
        extensions.append(Extension(
            name + '._' + name,
            [modpath('%s/_%s.m' % (name, name))],
            extra_compile_args=['-I' + modpath('objc')] + CFLAGS,
            extra_link_args=f + LDFLAGS,
            **deps(name)))
    extensions.extend(extras)
            
    if options.get('no_package'):
        p = []
    else:
        p = [name]
    packages, extensions = IfFramework(name + '.framework', p, extensions)
    PACKAGES[name] = packages, extensions
