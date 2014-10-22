'''
Wrappers for the framework "LatentSemanticMapping" on MacOSX 10.5 or later.

The Latent Semantic Mapping framework supports the classification of text and other token-based content into developer-defined categories.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks.

NOTE: Apple's documentation for this framework is very minimal at the moment,
making it very hard to actually use the framework.
'''
from pyobjc_setup import setup

setup(
    min_os_level='10.5',
    name='pyobjc-framework-LatentSemanticMapping',
    version="3.0.4",
    description = "Wrappers for the framework LatentSemanticMapping on Mac OS X",
    long_description=__doc__,
    packages = [ "LatentSemanticMapping" ],
    setup_requires = [
        'pyobjc-core>=3.0.4',
    ],
    install_requires = [
        'pyobjc-core>=3.0.4',
        'pyobjc-framework-Cocoa>=3.0.4',
    ],
)
