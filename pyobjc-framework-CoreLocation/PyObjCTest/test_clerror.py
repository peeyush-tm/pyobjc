
from PyObjCTools.TestSupport import *
from CoreLocation import *
import os

class TestCLError (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertIsInstance(kCLErrorDomain, unicode)

        self.assertEqual(kCLErrorLocationUnknown, 0)
        self.assertEqual(kCLErrorDenied, 1)
        self.assertEqual(kCLErrorNetwork, 2)
        self.assertEqual(kCLErrorHeadingFailure, 3)
        self.assertEqual(kCLErrorRegionMonitoringDenied, 4)
        self.assertEqual(kCLErrorRegionMonitoringFailure, 5)
        self.assertEqual(kCLErrorRegionMonitoringSetupDelayed, 6)
        self.assertEqual(kCLErrorRegionMonitoringResponseDelayed, 7)
        self.assertEqual(kCLErrorGeocodeFoundPartialResult, 9)
        self.assertEqual(kCLErrorGeocodeCanceled, 10)
        self.assertEqual(kCLErrorDeferredFailed, 11)
        self.assertEqual(kCLErrorDeferredNotUpdatingLocation, 12)
        self.assertEqual(kCLErrorDeferredAccuracyTooLow, 13)
        self.assertEqual(kCLErrorDeferredDistanceFiltered, 14)
        self.assertEqual(kCLErrorDeferredCanceled, 15)
        self.assertEqual(kCLErrorRangingUnavailable, 16)
        self.assertEqual(kCLErrorRangingFailure, 17)

        if int(os.uname()[2].split('.')[0]) < 12:
            self.assertEqual(kCLErrorFoundNoResult, 7)
            self.assertEqual(kCLErrorCanceled, 8)
        else:
            self.assertEqual(kCLErrorGeocodeFoundNoResult, 8)

    @min_os_level('10.7')
    @expectedFailure
    def testConstants10_7(self):
        self.assertIsInstance(kCLErrorUserInfoAlternateRegionKey, unicode)

if __name__ == "__main__":
    main()
