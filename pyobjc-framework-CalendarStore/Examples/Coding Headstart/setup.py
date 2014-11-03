"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="PyCalendarStore",
    app=["main.py"],
    data_files=["English.lproj"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-CalendarStore",
        "pyobjc-framework-Cocoa",
    ]
)
