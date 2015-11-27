import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKModifySubscriptionsOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKModifySubscriptionsOperation")
            self.assertIsInstance(CloudKit.CKModifySubscriptionsOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertResultIsBlock(CloudKit.CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock, b"v@@@")
            self.assertArgIsBlock(CloudKit.CKModifySubscriptionsOperation.setModifySubscriptionsCompletionBlock_, 0, b"v@@@")

if __name__ == "__main__":
    main()
