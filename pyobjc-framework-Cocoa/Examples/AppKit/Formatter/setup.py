"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="Formatter",
    app=["main.py"],
    data_files=["MainMenu.nib"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
