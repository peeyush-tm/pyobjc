'''
Wrappers for the "ExceptionHandling" framework on MacOSX. The ExceptionHandling
framework provides facilities for monitoring and debugging exceptional
conditions in Cocoa programs.

PyObjC also provides low-level debugging utilities beyond the core
ExceptionHandling framework in the module ``PyObjCTools.Debugging``.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from  pyobjc_setup import setup

VERSION="3.2a1"

setup(
    name='pyobjc-framework-ExceptionHandling',
    version=VERSION,
    description = "Wrappers for the framework ExceptionHandling on Mac OS X",
    long_description=__doc__,
    packages = [ "PyObjCTools", "ExceptionHandling" ],
    namespace_packages = [ "PyObjCTools" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
)
