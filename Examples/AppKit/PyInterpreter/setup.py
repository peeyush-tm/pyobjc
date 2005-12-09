"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(NSMainNibFile='PyInterpreter')
setup(
    app=["PyInterpreter.py"],
    data_files=["PyInterpreter.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
