import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit
    import Quartz

    class TestSKPhysicsWorld (TestCase):
        @min_os_level("10.9")
        def testMethods(self):
            self.assertArgIsBlock(SpriteKit.SKPhysicsWorld.enumerateBodiesAtPoint_usingBlock_, 1,
                    b'v@o^Z')
            self.assertArgIsBlock(SpriteKit.SKPhysicsWorld.enumerateBodiesInRect_usingBlock_, 1,
                    b'v@o^Z')
            self.assertArgIsBlock(SpriteKit.SKPhysicsWorld.enumerateBodiesAlongRayStart_end_usingBlock_, 2,
                    b'v@' + Quartz.CGPoint.__typestr__ + Quartz.CGVector.__typestr__ + b'o^Z')

            o = SpriteKit.SKPhysicsWorld.alloc().init()
            v = o.sampleFieldsAt_((9, 10, 11))
            self.assertIsInstance(v, tuple)
            self.assertEqual(len(v), 3)
            self.assertIsInstance(v[0], float)
            self.assertIsInstance(v[1], float)
            self.assertIsInstance(v[2], float)

        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('SKPhysicsContactDelegate')


if __name__ == "__main__":
    main()
