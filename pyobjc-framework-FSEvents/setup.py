'''
Wrappers for the "FSEvents" API in MacOS X. The functions in this framework
allow you to reliably observe changes to the filesystem, even when your
program is not running al the time.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

VERSION="3.2a1"

setup(
    min_os_level='10.5',
    name='pyobjc-framework-FSEvents',
    version=VERSION,
    description = "Wrappers for the framework FSEvents on Mac OS X",
    long_description=__doc__,
    packages = [ "FSEvents" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    ext_modules = [
        Extension("FSEvents._callbacks",
            [ "Modules/_callbacks.m" ],
        ),
    ],
)
