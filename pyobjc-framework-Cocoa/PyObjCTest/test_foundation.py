'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import Foundation
import os


class TestFoundation (TestCase):
    def testValues(self):
        self.assert_( hasattr(Foundation, 'NSTimeIntervalSince1970') )
        self.assert_( isinstance(Foundation.NSTimeIntervalSince1970, float) )
        self.assertEqual(Foundation.NSTimeIntervalSince1970, 978307200.0)

        if int(os.uname()[2].split('.')[0]) < 9:
            self.assert_( hasattr(Foundation, 'NSMaximumStringLength') )
            self.assert_( isinstance(Foundation.NSMaximumStringLength, (int, long)) )
        self.assert_( hasattr(Foundation, 'NSURLResponseUnknownLength') )
        self.assert_( isinstance(Foundation.NSURLResponseUnknownLength, (int, long)) )

    def testFunctions(self):
        self.assert_( hasattr(Foundation, 'NSStringFromSelector') )

    def testProtocols(self):
        self.assertFalse( hasattr(Foundation, 'protocols') )


    def test_structs(self):
        self.assert_( hasattr(Foundation, 'NSPoint') )
        o = Foundation.NSPoint()
        self.assert_( hasattr(o, 'x') )
        self.assert_( hasattr(o, 'y') )

        self.assert_( hasattr(Foundation, 'NSSize') )
        o = Foundation.NSSize()
        self.assert_( hasattr(o, 'width') )
        self.assert_( hasattr(o, 'height') )

        self.assert_( hasattr(Foundation, 'NSRange') )
        o = Foundation.NSRange()
        self.assert_( hasattr(o, 'location') )
        self.assert_( hasattr(o, 'length') )

        self.assert_( hasattr(Foundation, 'NSRect') )
        o = Foundation.NSRect()
        self.assert_( hasattr(o, 'origin') )
        self.assert_( hasattr(o, 'size') )
        self.assert_( isinstance(o.origin, Foundation.NSPoint) )
        self.assert_( isinstance(o.size, Foundation.NSSize) )

        self.assert_( hasattr(Foundation, 'NSAffineTransformStruct') )
        o = Foundation.NSAffineTransformStruct()
        self.assert_( hasattr(o, 'm11') )
        self.assert_( hasattr(o, 'm12') )
        self.assert_( hasattr(o, 'm21') )
        self.assert_( hasattr(o, 'm22') )
        self.assert_( hasattr(o, 'tX') )
        self.assert_( hasattr(o, 'tY') )


if __name__ == "__main__":
    main()
