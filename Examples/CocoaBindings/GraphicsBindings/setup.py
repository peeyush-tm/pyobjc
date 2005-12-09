"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=[u'GraphicsBindings', u'*'],
            CFBundleTypeName=u'GraphicsBindings File',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'GraphicsBindingsDocument',
        ),
    ],
)

setup(
    app=["GraphicsBindings.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
