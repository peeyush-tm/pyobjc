from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEVPNConnection (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NEVPNErrorConfigurationInvalid, 1)
            self.assertEqual(NetworkExtension.NEVPNErrorConfigurationDisabled, 2)
            self.assertEqual(NetworkExtension.NEVPNErrorConnectionFailed, 3)
            self.assertEqual(NetworkExtension.NEVPNErrorConfigurationStale, 4)
            self.assertEqual(NetworkExtension.NEVPNErrorConfigurationReadWriteFailed, 5)
            self.assertEqual(NetworkExtension.NEVPNErrorConfigurationUnknown, 6)

            self.assertIsInstance(NetworkExtension.NEVPNErrorDomain, unicode)
            self.assertIsInstance(NetworkExtension.NEVPNConfigurationChangeNotification, unicode)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NEVPNManager.loadFromPreferencesWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(NetworkExtension.NEVPNManager.removeFromPreferencesWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(NetworkExtension.NEVPNManager.saveToPreferencesWithCompletionHandler_, 0, b'v@')

            self.assertResultIsBOOL(NetworkExtension.NEVPNManager.isOnDemandEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEVPNManager.setOnDemandEnabled_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNManager.isEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEVPNManager.setEnabled_, 0)


if __name__ == "__main__":
    main()
