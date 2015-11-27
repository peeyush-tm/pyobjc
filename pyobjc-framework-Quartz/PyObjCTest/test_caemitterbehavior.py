from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAEmitterBehavior (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(CAEmitterBehavior.isEnabled)
        self.assertArgIsBOOL(CAAnimation.setEnabled_, 0)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCAEmitterBehaviorWave, unicode)
        self.assertIsInstance(kCAEmitterBehaviorDrag, unicode)
        self.assertIsInstance(kCAEmitterBehaviorAlignToMotion, unicode)
        self.assertIsInstance(kCAEmitterBehaviorValueOverLife, unicode)
        self.assertIsInstance(kCAEmitterBehaviorColorOverLife, unicode)
        self.assertIsInstance(kCAEmitterBehaviorLight, unicode)
        self.assertIsInstance(kCAEmitterBehaviorAttractor, unicode)

if __name__ == "__main__":
    main()
