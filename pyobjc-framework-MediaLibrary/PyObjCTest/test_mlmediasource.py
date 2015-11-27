import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import MediaLibrary

    class TestMLMediaSource (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MediaLibrary.MLMediaSource, objc.objc_class)

if __name__ == "__main__":
    main()
