import unittest, os
from CoreFoundation import *


class TestURLAccess (unittest.TestCase):
    def testConstants(self):
        self.failUnless( kCFURLUnknownError == -10  )
        self.failUnless( kCFURLUnknownSchemeError == -11    )
        self.failUnless( kCFURLResourceNotFoundError == -12 )
        self.failUnless( kCFURLResourceAccessViolationError == -13  )
        self.failUnless( kCFURLRemoteHostUnavailableError == -14    )
        self.failUnless( kCFURLImproperArgumentsError == -15    )
        self.failUnless( kCFURLUnknownPropertyKeyError == -16   )
        self.failUnless( kCFURLPropertyKeyUnavailableError == -17   )
        self.failUnless( kCFURLTimeoutError == -18 )

        self.failUnless( isinstance( kCFURLFileExists, unicode) )
        self.failUnless( isinstance( kCFURLFileDirectoryContents, unicode) )
        self.failUnless( isinstance( kCFURLFileLength, unicode) )
        self.failUnless( isinstance( kCFURLFileLastModificationTime, unicode) )
        self.failUnless( isinstance( kCFURLFilePOSIXMode, unicode) )
        self.failUnless( isinstance( kCFURLFileOwnerID, unicode) )
        self.failUnless( isinstance( kCFURLHTTPStatusCode, unicode) )
        self.failUnless( isinstance( kCFURLHTTPStatusLine, unicode) )


    def testFunctions(self):
        url = CFURLCreateWithFileSystemPath(None, __file__, kCFURLPOSIXPathStyle, False)

        val, errorCode = CFURLCreatePropertyFromResource(None, url, kCFURLFileExists, None)
        self.failUnless(isinstance(errorCode, (int, long)))
        self.failUnless(val is True)

        ok, data, properties, errorCode = CFURLCreateDataAndPropertiesFromResource(
                None, url, None, None, None, None)
        self.failUnless(ok)
        self.failUnless(isinstance(data, CFDataRef))
        self.failUnless(isinstance(properties, CFDictionaryRef))
        self.failUnless(isinstance(errorCode, (int, long)))
        self.failUnless(properties[kCFURLFileExists])

        url = CFURLCreateWithFileSystemPath(None, __file__ + "TEST", kCFURLPOSIXPathStyle, False)
        ok, errorCode = CFURLWriteDataAndPropertiesToResource(
                url, buffer("foobar"), None, None)
        self.failUnless(ok)
        self.failUnless(isinstance(errorCode, (int, long)))
        self.failUnless(os.path.exists(__file__ + "TEST"))
        data = open(__file__ + "TEST", 'r').read()
        self.failUnless(data == 'foobar')

        ok, errorCode = CFURLDestroyResource(url, None)
        self.failUnless(ok)
        self.failUnless(isinstance(errorCode, (int, long)))
        self.failIf(os.path.exists(__file__ + "TEST"))


            
                
if __name__ == "__main__":
    unittest.main()
