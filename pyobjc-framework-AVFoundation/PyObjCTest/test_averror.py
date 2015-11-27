from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVError (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVFoundationErrorDomain, unicode)

        self.assertIsInstance(AVFoundation.AVErrorDeviceKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorTimeKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorFileSizeKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorPIDKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorRecordingSuccessfullyFinishedKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorMediaTypeKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorMediaSubTypeKey, unicode)

        self.assertIsInstance(AVFoundation.AVErrorDiscontinuityFlagsKey, unicode)

        self.assertEqual(AVFoundation.AVErrorUnknown, -11800)
        self.assertEqual(AVFoundation.AVErrorOutOfMemory, -11801)
        self.assertEqual(AVFoundation.AVErrorSessionNotRunning, -11803)
        self.assertEqual(AVFoundation.AVErrorDeviceAlreadyUsedByAnotherSession, -11804)
        self.assertEqual(AVFoundation.AVErrorNoDataCaptured, -11805)
        self.assertEqual(AVFoundation.AVErrorSessionConfigurationChanged, -11806)
        self.assertEqual(AVFoundation.AVErrorDiskFull, -11807)
        self.assertEqual(AVFoundation.AVErrorDeviceWasDisconnected, -11808)
        self.assertEqual(AVFoundation.AVErrorMediaChanged, -11809)
        self.assertEqual(AVFoundation.AVErrorMaximumDurationReached, -11810)
        self.assertEqual(AVFoundation.AVErrorMaximumFileSizeReached, -11811)
        self.assertEqual(AVFoundation.AVErrorMediaDiscontinuity, -11812)
        self.assertEqual(AVFoundation.AVErrorMaximumNumberOfSamplesForFileFormatReached, -11813)
        self.assertEqual(AVFoundation.AVErrorDeviceNotConnected, -11814)
        self.assertEqual(AVFoundation.AVErrorDeviceInUseByAnotherApplication, -11815)
        self.assertEqual(AVFoundation.AVErrorDeviceLockedForConfigurationByAnotherProcess, -11817)

        self.assertEqual(AVFoundation.AVErrorExportFailed, -11820)
        self.assertEqual(AVFoundation.AVErrorDecodeFailed, -11821)
        self.assertEqual(AVFoundation.AVErrorInvalidSourceMedia, -11822)
        self.assertEqual(AVFoundation.AVErrorFileAlreadyExists, -11823)
        self.assertEqual(AVFoundation.AVErrorCompositionTrackSegmentsNotContiguous, -11824)
        self.assertEqual(AVFoundation.AVErrorInvalidCompositionTrackSegmentDuration, -11825)
        self.assertEqual(AVFoundation.AVErrorInvalidCompositionTrackSegmentSourceStartTime, -11826)
        self.assertEqual(AVFoundation.AVErrorInvalidCompositionTrackSegmentSourceDuration, -11827)
        self.assertEqual(AVFoundation.AVErrorFileFormatNotRecognized, -11828)
        self.assertEqual(AVFoundation.AVErrorFileFailedToParse, -11829)
        self.assertEqual(AVFoundation.AVErrorMaximumStillImageCaptureRequestsExceeded, -11830)
        self.assertEqual(AVFoundation.AVErrorContentIsProtected, -11831)
        self.assertEqual(AVFoundation.AVErrorNoImageAtTime, -11832)
        self.assertEqual(AVFoundation.AVErrorDecoderNotFound, -11833)
        self.assertEqual(AVFoundation.AVErrorEncoderNotFound, -11834)
        self.assertEqual(AVFoundation.AVErrorContentIsNotAuthorized, -11835)
        self.assertEqual(AVFoundation.AVErrorApplicationIsNotAuthorized, -11836)
        self.assertEqual(AVFoundation.AVErrorOperationNotSupportedForAsset, -11838)

        self.assertEqual(AVFoundation.AVErrorDecoderTemporarilyUnavailable, -11839)
        self.assertEqual(AVFoundation.AVErrorEncoderTemporarilyUnavailable, -11840)
        self.assertEqual(AVFoundation.AVErrorInvalidVideoComposition, -11841)
        self.assertEqual(AVFoundation.AVErrorReferenceForbiddenByReferencePolicy, -11842)
        self.assertEqual(AVFoundation.AVErrorInvalidOutputURLPathExtension, -11843)
        self.assertEqual(AVFoundation.AVErrorScreenCaptureFailed, -11844)
        self.assertEqual(AVFoundation.AVErrorDisplayWasDisabled, -11845)
        self.assertEqual(AVFoundation.AVErrorTorchLevelUnavailable, -11846)

        self.assertEqual(AVFoundation.AVErrorIncompatibleAsset, -11848)
        self.assertEqual(AVFoundation.AVErrorFailedToLoadMediaData, -11849)
        self.assertEqual(AVFoundation.AVErrorServerIncorrectlyConfigured, -11850)
        self.assertEqual(AVFoundation.AVErrorApplicationIsNotAuthorizedToUseDevice, -11852)
        self.assertEqual(AVFoundation.AVErrorFailedToParse, -11853)
        self.assertEqual(AVFoundation.AVErrorFileTypeDoesNotSupportSampleReferences, -11854)
        self.assertEqual(AVFoundation.AVErrorUndecodableMediaData, -11855)
        self.assertEqual(AVFoundation.AVErrorAirPlayControllerRequiresInternet, -11856)
        self.assertEqual(AVFoundation.AVErrorAirPlayReceiverRequiresInternet, -11857)
        self.assertEqual(AVFoundation.AVErrorVideoCompositorFailed, -11858)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVErrorPresentationTimeStampKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorPersistentTrackIDKey, unicode)
        self.assertIsInstance(AVFoundation.AVErrorFileTypeKey, unicode)


if __name__ == "__main__":
    main()
