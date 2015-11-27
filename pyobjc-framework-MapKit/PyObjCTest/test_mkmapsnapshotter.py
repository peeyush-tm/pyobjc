import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    MKMapSnapshotCompletionHandler = b'v@@'

    class TestMKMapSnapshotter (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKMapSnapshotter, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKMapSnapshotter.isLoading)
            #self.assertArgIsBOOL(MapKit.MKMapSnapshotter.setLoading_, 0)

            self.assertArgIsBlock(MapKit.MKMapSnapshotter.startWithCompletionHandler_, 0, MKMapSnapshotCompletionHandler)

            # XXX: Argument 0 is a dispatch queue, not wrapped...
            self.assertArgIsBlock(MapKit.MKMapSnapshotter.startWithQueue_completionHandler_, 1, MKMapSnapshotCompletionHandler)

if __name__ == "__main__":
    main()
