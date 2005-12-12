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

# core-tests don't need the class cache rebuild
extra_cmdclass.pop('build_ext')

from setuptools import setup, Extension, Distribution
import os

packages = ['PyObjCTests.objc.test']
extensions = []
for test_source in glob.glob(modpath('objc', 'test', '*.m')):
    name, ext = os.path.splitext(os.path.basename(test_source))

    if name != 'ctests':
        ext = Extension('PyObjCTests.objc.test.' + name,
            [test_source],
            extra_compile_args=['-I' + modpath('objc')] + CFLAGS,
            extra_link_args=ldflags('objc'))
    else:
        ext = Extension('PyObjCTests.objc.test.' + name,
            [test_source] + FFI_SOURCE,
            extra_compile_args=['-I' + modpath('objc')] + CFLAGS + FFI_CFLAGS,
            extra_link_args=ldflags('objc') + LDFLAGS)

    extensions.append(ext)

# The following line is needed to allow separate flat modules
# to be installed from a different folder
package_dir = dict([(pkg, libpath(pkg.replace('.', '/'))) for pkg in packages])

package_dir[''] = libpath()

dist = setup(
    name="pyobjc-core-tests",
    version=package_version(),
    description="Python<->ObjC Interoperability Module",
    long_description=LONG_DESCRIPTION,
    author="bbum, RonaldO, SteveM, LeleG, many others stretching back through the reaches of time...",
    author_email="pyobjc-dev@lists.sourceforge.net",
    url="http://pyobjc.sourceforge.net/",
    platforms=['MacOS X'],
    namespace_packages=['PyObjCTests'],
    ext_modules=extensions,
    packages=packages,
    package_dir=package_dir,
    cmdclass=extra_cmdclass,
    classifiers=CLASSIFIERS,
    license='MIT License',
    download_url='http://pyobjc.sourceforge.net/software/index.php',
    setup_requires=['pyobjc-core'],
    install_requires=['pyobjc-core'],
    extras_require={},
    entry_points={},
    zip_safe=False,
)
