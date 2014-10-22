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

setup(
    min_os_level='10.5',
    name='pyobjc-framework-FSEvents',
    version="3.0.4",
    description = "Wrappers for the framework FSEvents on Mac OS X",
    long_description=__doc__,
    packages = [ "FSEvents" ],
    setup_requires = [
        'pyobjc-core>=3.0.4',
    ],
    install_requires = [
        'pyobjc-core>=3.0.4',
        'pyobjc-framework-Cocoa>=3.0.4',
    ],
    ext_modules = [
        Extension("FSEvents._callbacks",
            [ "Modules/_callbacks.m" ],
        ),
    ],
)
