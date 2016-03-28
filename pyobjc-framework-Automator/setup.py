'''
Wrappers for the "Automator" framework on MacOSX. The Automator framework
supports the development of actions for the Automator application, as well
as the ability to run a workflow in developer applications. An action is
a bundle that, when loaded and run, performs a specific task.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    name='pyobjc-framework-Automator',
    version=VERSION,
    description = "Wrappers for the framework Automator on Mac OS X",
    long_description=__doc__,
    packages = [ "Automator" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
)
