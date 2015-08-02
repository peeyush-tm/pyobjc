from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKMatchmakerViewController (TestCase):
        @min_os_level('10.8')
        def testProtocols(self):
            objc.protocolNamed('GKMatchmakerViewControllerDelegate')

        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertIsInstance(GameCenter.GKMatchmakerViewController, objc.objc_class)

            self.assertResultIsBOOL(GameCenter.GKMatchmakerViewController.isHosted)
            self.assertArgIsBOOL(GameCenter.GKMatchmakerViewController.setHosted_, 0)
            self.assertArgIsBOOL(GameCenter.GKMatchmakerViewController.setHostedPlayer_connected_, 1)

        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertArgIsBOOL(GameCenter.GKMatchmakerViewController.setHostedPlayer_didConnect_, 1)

if __name__ == "__main__":
    main()
