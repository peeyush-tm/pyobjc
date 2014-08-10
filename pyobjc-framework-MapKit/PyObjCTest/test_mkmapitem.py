import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKMapItem (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKMapItem, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKMapItem.isCurrentLocation)
            self.assertResultIsBOOL(MapKit.MKMapItem.openInMapsWithLaunchOptions_))
            self.assertResultIsBOOL(MapKit.MKMapItem.openMapsWithItems_launchOptions_))

        @min_os_level("10.9")
        def testConstants(self):
            self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeKey, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsMapTypeKey, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsShowsTrafficKey, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeDriving, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeWalking, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsMapCenterKey, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsMapSpanKey, unicode)
            self.assertIsInstance(MapKit.MKLaunchOptionsCameraKey, unicode)

if __name__ == "__main__":
    main()
