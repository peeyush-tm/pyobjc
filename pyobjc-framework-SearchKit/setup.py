'''
Wrappers for the "SearchKit" framework on MacOSX. SearchKit is a content
indexing and search solution.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: These wrappers are pretty fragile, sadly enough not all run-time
information that needed to build reliable wrappers is exported from
the framework.
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.5',
    name='pyobjc-framework-SearchKit',
    version="3.0.4",
    description = "Wrappers for the framework SearchKit on Mac OS X",
    long_description=__doc__,
    packages = [ "SearchKit" ],
    setup_requires = [
        'pyobjc-core>=3.0.4',
    ],
    install_requires = [
        'pyobjc-core>=3.0.4',
        'pyobjc-framework-Cocoa>=3.0.4',
    ],
)
