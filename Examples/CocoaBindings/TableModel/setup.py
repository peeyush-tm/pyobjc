"""
Script for building the example, alternative to the Xcode project.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app=["__main__.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(plist='Info.plist')),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
