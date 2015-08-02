from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKGameCenterViewController (TestCase):
        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(GameCenter.GKGameCenterViewControllerStateDefault, -1)
            self.assertEqual(GameCenter.GKGameCenterViewControllerStateLeaderboards, 0)
            self.assertEqual(GameCenter.GKGameCenterViewControllerStateAchievements, 1)
            self.assertEqual(GameCenter.GKGameCenterViewControllerStateChallenges, 2)

        @min_os_level('10.9')
        def testProtocols10_9(self):
            objc.protocolNamed('GKGameCenterControllerDelegate')

if __name__ == "__main__":
    main()
