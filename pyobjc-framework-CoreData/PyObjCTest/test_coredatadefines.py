
from PyObjCTools.TestSupport import *
from CoreData import *

class TestCoreDataDefines (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSCoreDataVersionNumber, float)

        self.assertEqual(NSCoreDataVersionNumber10_4, 46.0)
        self.assertEqual(NSCoreDataVersionNumber10_4_3, 77.0)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSCoreDataVersionNumber10_5, 185.0)
        self.assertEqual(NSCoreDataVersionNumber10_5_3, 186.0)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSCoreDataVersionNumber10_7, 358.4)
        self.assertEqual(NSCoreDataVersionNumber10_7_2, 358.12)
        self.assertEqual(NSCoreDataVersionNumber10_7_3, 358.13)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(NSCoreDataVersionNumber10_8, 407.5)
        self.assertEqual(NSCoreDataVersionNumber10_8_2, 407.7)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertEqual(NSCoreDataVersionNumber10_9, 481.0)
        self.assertEqual(NSCoreDataVersionNumber10_9_2, 481.1)
        self.assertEqual(NSCoreDataVersionNumber10_9_3, 481.3)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertEqual(NSCoreDataVersionNumber10_10, 526.0)
        self.assertEqual(NSCoreDataVersionNumber10_10_2, 526.1)
        self.assertEqual(NSCoreDataVersionNumber10_10_3, 526.2)

if __name__ == "__main__":
    main()
