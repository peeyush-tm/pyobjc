'''
Wrappers for the "SyncServices" framework on MacOSX.

Sync Services is a framework containing all the components you need
to sync your applications and devices. If your application uses
Sync Services, user data can be synced with other applications and
devices on the same computer, or other computers over the network via
MobileMe.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-SyncServices',
    version="3.0.2",
    description = "Wrappers for the framework SyncServices on Mac OS X",
    packages = [ "SyncServices" ],
    setup_requires = [
        'pyobjc-core>=3.0.2',
    ],
    install_requires = [
        'pyobjc-core>=3.0.2',
        'pyobjc-framework-Cocoa>=3.0.2',
        'pyobjc-framework-CoreData>=3.0.2',
    ],
    ext_modules = [
        Extension("SyncServices._SyncServices",
            [ "Modules/_SyncServices.m" ],
            extra_link_args=["-framework", "SyncServices"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_SyncServices')
            ]
        ),
    ]
)
