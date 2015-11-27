from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetReaderOutput (TestCase):
    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetReaderOutput.alwaysCopiesSampleData)
        self.assertArgIsBOOL(AVFoundation.AVAssetReaderOutput.setAlwaysCopiesSampleData_, 0)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetReaderOutput.supportsRandomAccess)
        self.assertArgIsBOOL(AVFoundation.AVAssetReaderOutput.setSupportsRandomAccess_, 0)

if __name__ == "__main__":
    main()
