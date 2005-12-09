"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app=["main.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(plist=dict(
        CFBundleName='iClass',
    ))),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
