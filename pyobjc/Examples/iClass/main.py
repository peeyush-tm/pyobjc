"""
"""
from Cocoa.AppKit import NSApplicationMain
from Cocoa.Foundation import NSBundle
import sys
import os

print sys.path	
import datasource

print datasource.ClassesDataSource

print "Starting NSApplicationMain"
NSApplicationMain(sys.argv)
print "done"
