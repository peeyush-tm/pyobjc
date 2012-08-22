''' 
Wrappers for framework 'AppleScriptKit'. 

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-AppleScriptKit',
    version="2.4a0",
    description = "Wrappers for the framework AppleScriptKit on Mac OS X",
    packages = [ "AppleScriptKit" ],
    setup_requires = [
        'pyobjc-core>=2.4a0',
    ],
    install_requires = [ 
        'pyobjc-core>=2.4a0',
        'pyobjc-framework-Cocoa>=2.4a0',
    ],
)
