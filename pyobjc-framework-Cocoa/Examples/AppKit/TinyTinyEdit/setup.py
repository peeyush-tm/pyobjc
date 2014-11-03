"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=["txt", "text", "*"],
            CFBundleTypeName="Text File",
            CFBundleTypeRole="Editor",
            NSDocumentClass="TinyTinyDocument",
        ),
    ]
)

setup(
    name="Tiny Tiny Edit",
    app=["TinyTinyEdit.py"],
    data_files=["MainMenu.nib", "TinyTinyDocument.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
