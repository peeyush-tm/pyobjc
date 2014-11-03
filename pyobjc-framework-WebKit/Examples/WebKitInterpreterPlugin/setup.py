"""
Script for building the example.

Usage:
    python2 setup.py py2app
"""
from setuptools import setup

MIME = "application/x-pyobjc-demo-webkitinterpreter"
plist = dict(
    NSPrincipalClass="WebKitInterpreter",
    WebPluginName="WebKit PyInterpreter Plug-In",
    WebPluginDescription="PyObjC demo that embeds a Python interpreter",
    CFBundlePackageType="WBPL",
    WebPluginMIMETypes={
        MIME: dict(
            WebPluginExtensions=["webkitinterpreter"],
            WebPluginTypeDescription="WebKit PyInterpreter",
        ),
    },
)

setup(
    name="WebKitInterpreter",
    plugin = ["WebKitInterpreter.py"],
    options = dict(
        py2app=dict(
            plist=plist
        ),
    ),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-WebKit",
    ]
)
