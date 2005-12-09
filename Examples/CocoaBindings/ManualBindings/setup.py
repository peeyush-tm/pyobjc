"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app=["ManualBindings.py"],
    data_files=["English.lproj"],
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
