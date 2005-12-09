"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=[u'FilteringController', u'*'],
            CFBundleTypeName=u'FilteringController File',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'FilteringControllerDocument',
        ),
    ],
)

setup(
    app=["FilteringController.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
