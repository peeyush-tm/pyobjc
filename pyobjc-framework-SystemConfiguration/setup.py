''' 
Wrappers for framework 'SystemConfiguration'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension

setup(
    name='pyobjc-framework-SystemConfiguration',
    version="2.4",
    description = "Wrappers for the framework SystemConfiguration on Mac OS X",
    packages = [ "SystemConfiguration" ],
    setup_requires = [
        'pyobjc-core>=2.4',
    ],
    install_requires = [ 
        'pyobjc-core>=2.4',
        'pyobjc-framework-Cocoa>=2.4',
    ],
    ext_modules = [
        Extension('SystemConfiguration._manual',
                 [ 'Modules/_manual.m' ],
        ),
    ],
)
