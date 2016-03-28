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

VERSION="3.2a1"

setup(
    name='pyobjc-framework-InstallerPlugins',
    version=VERSION,
    description = "Wrappers for the framework InstallerPlugins on Mac OS X",
    long_description=__doc__,
    packages = [ "InstallerPlugins" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
)
