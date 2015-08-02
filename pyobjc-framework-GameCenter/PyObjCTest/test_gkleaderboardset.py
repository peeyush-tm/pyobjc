from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKLeaderboardSet (TestCase):
        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertArgIsBlock(GameCenter.GKLeaderboardSet.loadLeaderboardSetsWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLeaderboardSet.loadLeaderboardsWithCompletionHandler_, 0, b'v@@')

        @expectedFailure
        @min_os_level('10.10')
        def testMethods10_10_fail(self):
            self.assertArgIsBlock(GameCenter.GKLeaderboardSet.loadImageWithCompletionHandler_, 0, b'v@@')

if __name__ == "__main__":
    main()
