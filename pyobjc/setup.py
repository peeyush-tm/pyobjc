#!/usr/bin/env python

from distutils.core import setup, Extension
import os
import sys

# We need at least Python 2.3
req_ver = [ 2, 2]

if sys.platform == 'darwin' and \
   os.path.exists('/System/Library/Frameworks/Foundation.framework'):
	#
	# We're probably on MacOS X. We need a framework install of Python
	# to do anything remotely usefull, might as well check for that.
	#
	if os.path.islink(sys.executable):
		path = os.path.join(sys.executable,
			os.readlink(sys.executable));
	else:
		path = sys.executable
	path = os.path.normpath(path).lower()
#	if path.find('python.framework') == -1:
#		sys.stderr.write('PyObjC: Need framework install of python\n')
#		sys.exit(1)

if sys.version_info[0] < req_ver[0] or (
		sys.version_info[0] == req_ver[0] 
		and sys.version_info[1] < req_ver[1]):

	sys.stderr.write('PyObjC: Need at least Python %s\n'%('.'.join(req_ver)))
	sys.exit(1)


sourceFiles = [
	"Modules/objc/objc_util.m",
	"Modules/objc/objc_support.m",
	"Modules/objc/class-builder.m",
	"Modules/objc/class-list.m",
	"Modules/objc/ObjCPointer.m",
	"Modules/objc/objc-class.m",
	"Modules/objc/objc-object.m",
	"Modules/objc/super-call.m",
	"Modules/objc/selector.m",
	"Modules/objc/instance-var.m",
	"Modules/objc/OC_PythonInt.m",
	"Modules/objc/OC_PythonObject.m",
	"Modules/objc/OC_PythonString.m",
	"Modules/objc/register.m",
	"Modules/objc/pyobjc-api.m",
	"Modules/objc/module.m",
]

def IfFrameWork(name, packages, extensions):
	"""
	Return the packages and extensions if the framework exists, or
	two empty lists if not.
	"""
	if os.path.exists(os.path.join('/System/Library/Frameworks/', name)):
		return packages, extensions
	if os.path.exists(os.path.join('/Library/Frameworks/', name)):
		return packages, extensions
	return [], []


CorePackages = [ 'objc' ]
CoreExtensions =  [
	Extension("objc._objc", sourceFiles,
		   extra_compile_args=[
			"-g", "-O0",
			"-DOBJC_PARANOIA_MODE",
			"-DPyOBJC_UNIQUE_PROXY",
			"-DMACOSX",
		   ],
		   extra_link_args=[
			'-g', '-framework', 'AppKit'
		   ]),
	]
CocoaPackages = [ 'Cocoa', 'Cocoa.Foundation', 'Cocoa.AppKit' ]
CocoaExtensions = [
	  Extension("Cocoa.Foundation._Foundation", 
		   ["Modules/Cocoa/_Foundation.m"],
		   extra_compile_args=[
			"-g", "-IModules/objc",  
		   ],
		   extra_link_args=[
			'-framework', 'Foundation',
		   ]),
	  Extension("Cocoa.AppKit._AppKit", 
		   ["Modules/Cocoa/_AppKit.m"],
		   extra_compile_args=[
			"-g", "-IModules/objc", 
		   ],
		   extra_link_args=[
			'-framework', 'AppKit'
		   ]),
	  Extension("objc._FoundationMapping", 
		   ["Modules/Cocoa/_FoundationMapping.m"],
		   extra_compile_args=[
			"-g", "-IModules/objc", 
		   ],
		   extra_link_args=[
			'-framework', 'Foundation',
		   ]),
	  ]

# The AdressBook module is only installed when the user actually has the
# AddressBook framework.
AddressBookPackages, AddressBookExtensions = \
	IfFrameWork('AddressBook.framework', [ 'AddressBook' ], [])

try:
    setup (name = "pyobjc",
           version = "$Id: setup.py,v 1.4.2.4 2002/09/23 15:59:54 bbum Exp $",
           description = "Python<->ObjC Interoperability Module",
           author = "bbum, SteveM, many others stretching back through the reachtes of time...",
           author_email = "oussoren@cistron.nl", 
	   url = "http://pyobjc.sourceforge.net/",
           ext_modules = (
	     		   CoreExtensions 
	   		 + CocoaExtensions 
			 + AddressBookExtensions 
			 ),
	   packages = CorePackages + CocoaPackages + AddressBookPackages,
	   package_dir = { '':'Lib' }
           )

except:
    import sys
    import traceback
    traceback.print_exc()
