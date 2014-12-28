import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKGeodesicPolyline (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKGeodesicPolyline, objc.objc_class)

            self.assertArgSizeInArg(MapKit.MKGeodesicPolyline.polylineWithPoints_count_, 0, 1)
            self.assertArgIsIn(MapKit.MKGeodesicPolyline.polylineWithPoints_count_, 0)

            self.assertArgSizeInArg(MapKit.MKGeodesicPolyline.polylineWithCoordinates_count_, 0, 1)
            self.assertArgIsIn(MapKit.MKGeodesicPolyline.polylineWithCoordinates_count_, 0)

if __name__ == "__main__":
    main()