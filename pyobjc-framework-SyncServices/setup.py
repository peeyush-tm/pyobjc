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

VERSION="3.2a1"

setup(
    name='pyobjc-framework-SyncServices',
    version=VERSION,
    description = "Wrappers for the framework SyncServices on Mac OS X",
    long_description=__doc__,
    packages = [ "SyncServices" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
        'pyobjc-framework-CoreData>=' + VERSION,
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
