# Script to collect all method signatures in Cocoa
#
# TODO:
# - simplify signatures (remove additional information in the signature)
# - add list of usefull signatures

import objc

NSBundle = objc.lookup_class('NSBundle')

def load_bundle(path):
	NSBundle.bundleWithPath_(path).load()         
	classes = [ cls 
			for cls in objc.class_list() 
			if path == NSBundle.bundleForClass_(cls).bundlePath() ]
	return classes                          

#print objc.class_list()


load_bundle('/System/Library/Frameworks/Foundation.framework')
load_bundle('/System/Library/Frameworks/AppKit.framework')


signatures = {}
for cls in objc.class_list():
	for nm in dir(cls):
		try:
			signatures[getattr(cls, nm).signature] = 1
		except:
			pass

signatures = signatures.keys()
signatures.sort()
print '\n'.join(signatures)
