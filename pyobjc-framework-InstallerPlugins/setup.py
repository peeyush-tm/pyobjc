'''
Wrappers for the "InstallerPlugins" framework on MacOSX. This framework
allows you to develop plugin's for the "Installer.app" application, and those
make it possible to add new functionality to ".pkg" and ".mpkg" installers
on MacOSX.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import *

setup(
    name='pyobjc-framework-InstallerPlugins',
    version="3.0.4",
    description = "Wrappers for the framework InstallerPlugins on Mac OS X",
    long_description=__doc__,
    packages = [ "InstallerPlugins" ],
    setup_requires = [
        'pyobjc-core>=3.0.4',
    ],
    install_requires = [
        'pyobjc-core>=3.0.4',
        'pyobjc-framework-Cocoa>=3.0.4',
    ],
)
