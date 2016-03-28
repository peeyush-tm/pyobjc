'''
Wrappers for the "DictionaryServices" framework on MacOSX 10.5 or later.

Dictionary Services lets you create your own custom dictionaries that users
can access through the Dictionary application. You also use these services to
access dictionaries programatically and to support user access to dictionary
look-up through a contextual menu.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    min_os_level='10.5',
    name='pyobjc-framework-DictionaryServices',
    version=VERSION,
    description = "Wrappers for the framework DictionaryServices on Mac OS X",
    long_description=__doc__,
    packages = [ "DictionaryServices" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
)
