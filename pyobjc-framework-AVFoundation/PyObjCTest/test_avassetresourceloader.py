from PyObjCTools.TestSupport import *

import AVFoundation
import objc

class TestAVAssetResourceLoaderHelper (AVFoundation.NSObject):
    def resourceLoader_shouldWaitForLoadingOfRequestedResource_(self, rl, r): return 1
    def resourceLoader_shouldWaitForRenewalOfRequestedResource_(self, rl, r): return 1
    def resourceLoader_shouldWaitForResponseToAuthenticationChallenge_(self, rl, r): return 1

class TestAVAssetResourceLoader (TestCase):
    @min_os_level('10.9')
    def testProtocols(self):
        objc.protocolNamed('AVAssetResourceLoaderDelegate')

        self.assertResultHasType(TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForLoadingOfRequestedResource_, objc._C_NSBOOL)

    @min_os_level('10.10')
    def testProtocols10_10(self):
        self.assertResultHasType(TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForRenewalOfRequestedResource_, objc._C_NSBOOL)
        self.assertResultHasType(TestAVAssetResourceLoaderHelper.resourceLoader_shouldWaitForResponseToAuthenticationChallenge_, objc._C_NSBOOL)

    @min_os_level('10.9')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetResourceLoadingRequest.isFinished)

        self.assertResultIsBOOL(AVFoundation.AVAssetResourceLoadingRequest.isCancelled)

        self.assertResultIsBOOL(AVFoundation.AVAssetResourceLoadingContentInformationRequest.isByteRangeAccessSupported)
        self.assertArgIsBOOL(AVFoundation.AVAssetResourceLoadingContentInformationRequest.setByteRangeAccessSupported_, 0)

        self.assertArgIsOut(AVFoundation.AVAssetResourceLoadingRequest.streamingContentKeyRequestDataForApp_contentIdentifier_options_error_, 3)

if __name__ == "__main__":
    main()
