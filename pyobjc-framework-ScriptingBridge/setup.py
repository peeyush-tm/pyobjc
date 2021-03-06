'''
Wrappers for the "ScriptingBrige" framework on MacOSX 10.5 or later. This
framework provides an easy way to use the scripting functionality of
applications ("AppleScript") from Cocoa applications.

The functionality of this framework is comparable to that off "appscript",
although the latter is better tuned for use in Python applications and is
available on MacOSX 10.4 as well.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    min_os_level='10.5',
    name='pyobjc-framework-ScriptingBridge',
    version=VERSION,
    description = "Wrappers for the framework ScriptingBridge on Mac OS X",
    long_description=__doc__,
    packages = [ "ScriptingBridge" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    ext_modules = [
        Extension("ScriptingBridge._ScriptingBridge",
            [ "Modules/_ScriptingBridge.m" ],
            extra_link_args=["-framework", "ScriptingBridge"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_ScriptingBridge')
            ]
        ),
    ]
)
