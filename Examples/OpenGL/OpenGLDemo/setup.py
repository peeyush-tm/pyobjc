"""
Script for building the example.

Usage:
    python setup.py py2app
"""
try:
    import OpenGL.GL
except ImportError:
    raise SystemExit("This example requires pyOpenGL, which is not installed")

from setuptools import setup

plist = dict(NSMainNibFile='OpenGLDemo')
setup(
    app=['OpenGLDemo.py'],
    data_files=["OpenGLDemo.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=["py2app"],
    install_requires=["pyobjc"],
)
