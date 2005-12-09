"""
Script for building the example.

Usage:
    python setup.py py2app
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
    app=["TinyTinyEdit.py"],
    data_files=["MainMenu.nib", "TinyTinyDocument.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
