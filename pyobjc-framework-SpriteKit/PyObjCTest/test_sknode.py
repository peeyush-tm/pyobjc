import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import SpriteKit
    class TestSKNode (TestCase):
        @min_os_level('10.9')
        def testConstants(self):
            self.assertEqual(SpriteKit.SKBlendModeAlpha, 0)
            self.assertEqual(SpriteKit.SKBlendModeAdd, 1)
            self.assertEqual(SpriteKit.SKBlendModeSubtract, 2)
            self.assertEqual(SpriteKit.SKBlendModeMultiply, 3)
            self.assertEqual(SpriteKit.SKBlendModeMultiplyX2, 4)
            self.assertEqual(SpriteKit.SKBlendModeScreen, 5)
            self.assertEqual(SpriteKit.SKBlendModeReplace, 6)

        @min_os_level("10.9")
        def testMethods(self):
            self.assertIsInstance(SpriteKit.SKNode, objc.objc_class)

            self.assertArgIsBOOL(SpriteKit.SKNode.setPaused_, 0)
            self.assertResultIsBOOL(SpriteKit.SKNode.isPaused)
            self.assertArgIsBOOL(SpriteKit.SKNode.setHidden_, 0)
            self.assertResultIsBOOL(SpriteKit.SKNode.isHidden)
            self.assertArgIsBOOL(SpriteKit.SKNode.setUserInteractionEnabled_, 0)
            self.assertResultIsBOOL(SpriteKit.SKNode.isUserInteractionEnabled)
            self.assertResultIsBOOL(SpriteKit.SKNode.inParentHierarchy_)
            self.assertResultIsBOOL(SpriteKit.SKNode.hasActions)
            self.assertResultIsBOOL(SpriteKit.SKNode.containsPoint_)
            self.assertResultIsBOOL(SpriteKit.SKNode.intersectsNode_)

            self.assertArgIsBlock(SpriteKit.SKNode.enumerateChildNodesWithName_usingBlock_, 1, b'v@o^Z')
            self.assertArgIsBlock(SpriteKit.SKNode.runAction_completion_, 1, b'v')

if __name__ == "__main__":
    main()
