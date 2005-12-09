"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from setuptools import setup
import py2app

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=[u'Bookmarks', u'*'],
            CFBundleTypeName=u'Bookmarks File',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'BookmarksDocument',
        ),
    ],
)

setup(
    app=["Bookmarks.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
