from PyObjCTools.TestSupport import *
import objc
import sys

import SceneKit

class TestSCNPhysicsBody (TestCase):
    def test_constants(self):
        self.assertEqual(SceneKit.SCNPhysicsBodyTypeStatic, 0)
        self.assertEqual(SceneKit.SCNPhysicsBodyTypeDynamic, 1)
        self.assertEqual(SceneKit.SCNPhysicsBodyTypeKinematic, 2)

        self.assertEqual(SceneKit.SCNPhysicsCollisionCategoryDefault, 1 << 0)
        self.assertEqual(SceneKit.SCNPhysicsCollisionCategoryStatic, 1 << 1)
        self.assertEqual(SceneKit.SCNPhysicsCollisionCategoryAll, (sys.maxsize * 2) + 1)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.isResting)

        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setAllowsResting_ 0)
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.allowsResting)

        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.applyForce_impulse_, 1)
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.applyForce_atPosition_impulse_, 2)
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.applyTorque_impulse_, 1)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setUsesDefaultMomentOfInertia_ 0)
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.usesDefaultMomentOfInertia)

        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setAffectedByGravity_ 0)
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.affectedByGravity)

if __name__ == "__main__":
    main()
