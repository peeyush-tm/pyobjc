from PyObjCTools.TestSupport import *

import StoreKit

class TestSKDownload (TestCase):
    def test_constants(self):
        self.assertEqual(StoreKit.SKDownloadStateWaiting, 0)
        self.assertEqual(StoreKit.SKDownloadStateActive, 1)
        self.assertEqual(StoreKit.SKDownloadStatePaused, 2)
        self.assertEqual(StoreKit.SKDownloadStateFinished, 3)
        self.assertEqual(StoreKit.SKDownloadStateFailed, 4)
        self.assertEqual(StoreKit.SKDownloadStateCancelled, 5)

if __name__ == "__main__":
    main()

