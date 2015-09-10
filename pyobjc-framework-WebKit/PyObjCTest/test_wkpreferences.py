from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str


class TestWKPreferences (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKPreferences.javaScriptEnabled)
        self.assertArgIsBOOL(WKPreferences.setJavaScriptEnabled_, 0)
        self.assertResultIsBOOL(WKPreferences.javaScriptCanOpenWindowsAutomatically)
        self.assertArgIsBOOL(WKPreferences.setJavaScriptCanOpenWindowsAutomatically_, 0)
        self.assertResultIsBOOL(WKPreferences.javaEnabled)
        self.assertArgIsBOOL(WKPreferences.setJavaEnabled_, 0)
        self.assertResultIsBOOL(WKPreferences.plugInsEnabled)
        self.assertArgIsBOOL(WKPreferences.setPlugInsEnabled_, 0)


if __name__ == "__main__":
    main()
