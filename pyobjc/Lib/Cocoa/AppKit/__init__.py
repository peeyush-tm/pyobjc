"""
Python mapping for the Cocoa AppKit.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

# We first register special methods signatures with the runtime. The module
# is not used for anything else.
try:
	import _AppKitSignatures as dummy
	del dummy
except ImportError:
	pass

try:
	from Cocoa.AppKit._AppKit 		import *
except ImportError:
	pass


try:
	# We try to import a module containing support code, the code
	# is only ever used from the C side.
	import Cocoa.AppKit._AppKitMapping 
except ImportError:
	pass

# Load the Cocoa bundle, and gather all classes defined there
import Cocoa.Foundation
class_list = Cocoa.Foundation.load_bundle(
	'/System/Library/Frameworks/AppKit.framework')
gl = globals()
for cls in class_list:
	gl[cls.__name__] = cls

# clean-up after ourselves.
del class_list
del cls
del gl
del Cocoa.Foundation

# Define usefull utility methods here
