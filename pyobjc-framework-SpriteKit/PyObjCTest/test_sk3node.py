import sys
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


if sys.maxsize > 2 ** 32:
    import SpriteKit

    class TestSK3Node (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(SpriteKit.SK3Node, objc.objc_class)

if __name__ == "__main__":
    main()
