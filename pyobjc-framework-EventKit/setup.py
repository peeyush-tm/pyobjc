'''
Wrappers for the "EventKit" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

setup(
    name='pyobjc-framework-EventKit',
    version="3.1b1",
    description = "Wrappers for the framework Accounts on Mac OS X",
    long_description=__doc__,
    packages = [ "EventKit" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
    ],
    min_os_level="10.8",
)
