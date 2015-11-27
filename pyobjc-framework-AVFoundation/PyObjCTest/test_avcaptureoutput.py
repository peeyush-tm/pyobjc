from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVCaptureOutputHelper (AVFoundation.NSObject):
    def captureOutputShouldProvideSampleAccurateRecordingStart_(self, a): return 1


class TestAVCaptureOutput (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames)
        self.assertArgIsBOOL(AVFoundation.AVCaptureVideoDataOutput.setAlwaysDiscardsLateVideoFrames_, 0)

        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecording)
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecordingPaused)

        self.assertResultIsBOOL(TestAVCaptureOutputHelper.captureOutputShouldProvideSampleAccurateRecordingStart_)

        self.assertResultIsBOOL(AVFoundation.AVCaptureStillImageOutput.isCapturingStillImage)
        self.assertArgIsBlock(AVFoundation.AVCaptureStillImageOutput.captureStillImageAsynchronouslyFromConnection_completionHandler_, 1,
                b'v@@')

    def testProtocols(self):
        objc.protocolNamed('AVCaptureVideoDataOutputSampleBufferDelegate')
        objc.protocolNamed('AVCaptureAudioDataOutputSampleBufferDelegate')
        objc.protocolNamed('AVCaptureFileOutputRecordingDelegate')
        objc.protocolNamed('AVCaptureFileOutputDelegate')
        objc.protocolNamed('AVCaptureMetadataOutputObjectsDelegate')

if __name__ == "__main__":
    main()
