#!/usr/bin/env python

import os, sys
__file__ = os.path.abspath(__file__)
dn = os.path.dirname
SRCPATH = dn(dn(dn(__file__)))
sys.path.insert(0, SRCPATH)
os.chdir(SRCPATH)

import ez_setup
ez_setup.use_setuptools()

import sys
import os
import glob
import site

# Add our utility library to the path
site.addsitedir(os.path.abspath('source-deps'))
sys.path.insert(1, 'setup-lib')

from pyobjc_commands import extra_cmdclass
from if_framework import *
from compile_ffi import *
from pyobjc_metadata import *
from srcpath import srcpath, libpath, modpath, buildpath

from setuptools import setup
import os

packages = ['PyObjCTools.XcodeSupport']
extensions = []

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, libpath(pkg.replace('.', '/'))) for pkg in packages])

package_dir[''] = libpath()

dist = setup(
    name="pyobjc-XcodeSupport",
    version=package_version(),
    description="Python<->ObjC Interoperability Module",
    long_description=LONG_DESCRIPTION,
    author="bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email="pyobjc-dev@lists.sourceforge.net",
    url="http://pyobjc.sourceforge.net/",
    platforms=['MacOS X'],
    namespace_packages=['PyObjCTools'],
    ext_modules=extensions,
    packages=packages,
    package_dir=package_dir,
    cmdclass=extra_cmdclass,
    classifiers=CLASSIFIERS,
    license='MIT License',
    download_url='http://pyobjc.sourceforge.net/software/index.php',
    setup_requires=[],
    install_requires=[
        'pyobjc-core',
        'pyobjc-macosx-10_3',
        'pyobjc-macosx-10_4',
        "altgraph>=0.6.6,==dev",
        'py2app>=0.3.dev-r610,==dev',
        'bdist_mpkg>=0.3,==dev',
    ],
    extras_require={},
    entry_points={},
    zip_safe=True,
)
