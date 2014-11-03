"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    CFBundleIdentifier="net.sf.pyobjc.RemotePyInterpreter",
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeExtensions=[
                "RemotePyInterpreter",
                "*",
            ],
            CFBundleTypeName="RemotePyInterpreter Session",
            CFBundleTypeRole="Editor",
            NSDocumentClass="RemotePyInterpreterDocument",
        ),
    ],
)

REMOTE_REQUIREMENTS = [
    "tcpinterpreter",
    "netrepr",
    "remote_console",
    "remote_pipe",
    "remote_bootstrap"
]

DATA_FILES = ["English.lproj"] + [(s + ".py") for s in REMOTE_REQUIREMENTS]

setup(
    app=["RemotePyInterpreter.py"],
    data_files=DATA_FILES,
    options=dict(py2app=dict(plist=plist)),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
