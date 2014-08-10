'''
Wrappers for the "MediaLibrary" framework on MacOS X introduced in Mac OS X 10.9.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-MediaLibrary',
    version="3.1",
    description = "Wrappers for the framework MediaLibrary on Mac OS X",
    packages = [ "MediaLibrary" ],
    setup_requires = [
        'pyobjc-core>=3.1',
    ],
    install_requires = [
        'pyobjc-core>=3.1',
        'pyobjc-framework-Cocoa>=3.1',
        'pyobjc-framework-Quartz>=3.1',
    ],
    ext_modules = [
        Extension("MediaLibrary._MediaLibrary",
            [ "Modules/_MediaLibrary.m" ],
            extra_link_args=["-framework", "MediaLibrary"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_MediaLibrary')
            ]
        ),
    ],
)
