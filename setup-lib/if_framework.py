import sys, os
__all__ = ['IfFramework', 'CFLAGS', 'ALL_LDFLAGS', 'LDFLAGS', 'frameworks']

# If true we'll build universal binaries on systems with the 10.4u SDK running
# OS X 10.4 or later.
# 
# NOTE: This is an experimental feature.
AUTO_UNIVERSAL = False

# On GNUstep we can read some configuration from the environment.
gs_root = os.environ.get('GNUSTEP_SYSTEM_ROOT')

ALL_LDFLAGS = {}
LDFLAGS = []

def frameworks(*args):
    lst = []
    for arg in args:
        lst.extend(['-framework', arg])
    return lst

def depends(name, fmwks=()):
    ALL_LDFLAGS[name] = frameworks(*fmwks)

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

    depends('objc',
        ['Foundation', 'Carbon'])
    depends('CoreFoundation',
        ['CoreFoundation', 'Foundation'])
    depends('Foundation',
        ['CoreFoundation', 'Foundation'])
    depends('AppKit',
        ['CoreFoundation', 'AppKit'])
    depends('AddressBook',
        ['CoreFoundation', 'AddressBook', 'Foundation'])
    depends('InterfaceBuilder',
        ['CoreFoundation', 'InterfaceBuilder', 'Foundation'])
    depends('SecurityInterface',
        ['CoreFoundation', 'SecurityInterface', 'Foundation'])
    depends('ExceptionHandling',
        ['CoreFoundation', 'ExceptionHandling', 'Foundation'])
    depends('PreferencePanes',
        ['CoreFoundation', 'PreferencePanes', 'Foundation'])
    depends('SenTestingKit',
        ['SenTestingKit', 'Foundation'])
    depends('WebKit',
        ['WebKit', 'Foundation'])
    depends('XgridFoundation',
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

CFLAGS.append('-Ibuild/codegen/')
