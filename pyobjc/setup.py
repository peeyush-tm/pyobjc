#!/usr/bin/env python.exe

from distutils.core import setup, Extension

sourceFiles = [
               "OC_PythonInt.m",
               "OC_PythonObject.m",
               "OC_PythonString.m",
               "ObjC.m",
               "ObjCMethod.m",
               "ObjCClass.m",
               "ObjCIvar.m",
               "ObjCObject.m",
               "ObjCPointer.m",
	       "class-builder.m",
	       "method-dispatcher.m",
	       "pyobjc-api.m",
	       "register.m",
               "objc_support.m"]

try:
    setup (name = "pyobjc",
           version = "0.6.90",
           description = "Python<->ObjC Interoperability Module",
           author = "bbum, SteveM, many others stretching back through the reaches of time...",
           author_email = "bbum@codefab.com",
           url = "http://pyobjc.sourceforge.net/",
           ext_modules = [Extension("pyobjc", sourceFiles,
				   extra_compile_args=["-g"]) ],
	   packages = ['Cocoa'],
	   package_dir = { '':'Examples' }
           )
except:
    import sys
    import traceback
    traceback.print_exc()
