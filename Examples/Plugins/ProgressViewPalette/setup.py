"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

plist = dict(
    NSPrincipalClass='ProgressViewPalette',
)

setup(
    plugin=['ProgressViewPalette.py'],
    data_files=['English.lproj', 'palette.table'],
    options=dict(py2app=dict(
        extension='.palette',
        plist=plist,
    )),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
