"""
Script for building the example.

Usage:
    python setup.py py2app
""" 
from setuptools import setup

plist = dict(NSMainNibFile="ClassBrowser")
setup(
    app=["ClassBrowser.py"],
    data_files=["ClassBrowser.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
