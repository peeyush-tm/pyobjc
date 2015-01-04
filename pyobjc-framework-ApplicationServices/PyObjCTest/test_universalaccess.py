import HIServices
from PyObjCTools.TestSupport import *

class TestUniversalAccess (TestCase):
    def testConstants(self):
        self.assertEqual(HIServices.kUAZoomFocusTypeOther, 0)
        self.assertEqual(HIServices.kUAZoomFocusTypeInsertionPoint, 1)

    def testFunctions(self):
        self.assertResultIsBOOL(HIServices.UAZoomEnabled)

        self.assertArgIsIn(HIServices.UAZoomChangeFocus, 0)
        self.assertArgIsIn(HIServices.UAZoomChangeFocus, 1)

if __name__ == "__main__":
    main()
