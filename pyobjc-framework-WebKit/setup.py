'''
Wrappers for the "WebKit" and "JavaScriptCore" frameworks on MacOSX. The
WebKit framework contains the views and support classes for creating a
browser. The JavaScriptCore framework implements a JavaScript interpreter.

These wrappers don't include documentation, please check Apple's documention
for information on how to use these frameworks and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-WebKit',
    version=VERSION,
    description = "Wrappers for the framework WebKit on Mac OS X",
    long_description=__doc__,
    packages = [ "WebKit", "JavaScriptCore" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    ext_modules = [
        Extension("WebKit._WebKit",
            [ "Modules/_WebKit.m" ],
            extra_link_args=["-framework", "WebKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_WebKit')
            ]
        ),
    ]
)
