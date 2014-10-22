'''
Wrappers for framework 'ServerNotification' on MacOSX 10.6. This framework
contains the class NSServerNotificationCenter which provides distributed
notifications over the Extensible Messaging and Presence Protocol (XMPP).

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.6',
    max_os_level='10.8',
    name='pyobjc-framework-ServerNotification',
    version="3.0.4",
    description = "Wrappers for the framework ServerNotification on Mac OS X",
    long_description=__doc__,
    packages = [ "ServerNotification" ],
    setup_requires = [
        'pyobjc-core>=3.0.4',
    ],
    install_requires = [
        'pyobjc-core>=3.0.4',
        'pyobjc-framework-Cocoa>=3.0.4',
    ],
)
