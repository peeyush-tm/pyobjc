'''
PyObjC wrappers for the framework "CFNetwork", part of "CoreServices" on
MacOSX.

The CFNetwork framework provides a library of abstractions for networking
protocols. The most interesting bits for Python programmers are the
API's for working with proxy autoconfiguration and the API's for networking
diagnotics.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

VERSION="3.2a1"

setup(
    name='pyobjc-framework-CFNetwork',
    version=VERSION,
    description = "Wrappers for the framework CFNetwork on Mac OS X",
    long_description=__doc__,
    packages = [ "CFNetwork" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    ext_modules = [
        Extension("CFNetwork._manual",
            ["Modules/_manual.m"],
            extra_link_args=['-framework', 'CoreServices'],
        ),
    ],
)
