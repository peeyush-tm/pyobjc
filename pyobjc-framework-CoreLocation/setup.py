'''
Wrappers for framework 'CoreLocation' on MacOSX 10.6. This framework provides
an interface for dealing with the physical location of a machine, which allows
for geo-aware applications.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    min_os_level='10.6',
    name='pyobjc-framework-CoreLocation',
    version=VERSION,
    description = "Wrappers for the framework CoreLocation on Mac OS X",
    long_description=__doc__,
    packages = [ "CoreLocation" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    ext_modules = [
        Extension("CoreLocation._CoreLocation",
                [ "Modules/_CoreLocation.m" ],
                extra_link_args=["-framework", "CoreLocation"],
                depends=[
                    os.path.join('Modules', fn)
                        for fn in os.listdir('Modules')
                        if fn.startswith('_CoreLocation')
                ]
        ),
    ]
)
