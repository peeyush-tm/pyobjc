from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str


class TestWKError (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(WKErrorDomain, unicode)

        self.assertEqual(WKErrorUnknown, 1)
        self.assertEqual(WKErrorWebContentProcessTerminated, 2)
        self.assertEqual(WKErrorWebViewInvalidated, 3)
        self.assertEqual(WKErrorJavaScriptExceptionOccurred, 4)


if __name__ == "__main__":
    main()
