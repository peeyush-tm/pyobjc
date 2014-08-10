import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKAsset (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKDiscoveredUserInfo")
            self.assertIsInstance(CloudKit.CKDiscoveredUserInfo, objc.objc_class)

if __name__ == "__main__":
    main()
