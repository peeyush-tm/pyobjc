#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

import sys
import os
import glob
import site
import pkg_resources

sys.path.insert(1, 'setup-lib')
from pyobjc_metadata import *

extra_cmdclass = {}
packages = []
extensions = []
package_dir = {'': 'Lib'}
requirements = [
    "pyobjc-core",
    "pyobjc-macosx-10_3",
]
plat = pkg_resources.get_platform().split('-')
if plat[0] == 'macosx':
    if map(int, plat[1].split('.')[:2]) > [10, 3]:
        requirements.extend([
            'pyobjc-XcodeSupport',
            'pyobjc-macosx-10_4',
        ])

extras = {}
for path in glob.glob('subprojects/pyobjc-*'):
    sub = os.path.basename(path)
    name = sub[len('pyobjc-')]
    extras[sub] = [name]

dist = setup(
    name="pyobjc",
    version=package_version(),
    description="Python<->ObjC Interoperability Module",
    long_description=LONG_DESCRIPTION,
    author="bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email="pyobjc-dev@lists.sourceforge.net",
    url="http://pyobjc.sourceforge.net/",
    platforms=['MacOS X'],
    ext_modules=extensions,
    packages=packages,
    package_dir=package_dir,
    cmdclass=extra_cmdclass,
    classifiers=CLASSIFIERS,
    license='MIT License',
    download_url='http://pyobjc.sourceforge.net/software/index.php',
    install_requires=requirements,
    extras_require=extras,
    zip_safe=True,
)
