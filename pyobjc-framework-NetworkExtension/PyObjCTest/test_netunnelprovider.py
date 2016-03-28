from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEAppProxyFlow (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NETunnelProviderErrorNetworkSettingsInvalid, 1)
            self.assertEqual(NetworkExtension.NETunnelProviderErrorNetworkSettingsCanceled, 2)
            self.assertEqual(NetworkExtension.NETunnelProviderErrorNetworkSettingsFailed, 3)

            self.assertEqual(NetworkExtension.NETunnelProviderRoutingMethodDestinationIP, 1)
            self.assertEqual(NetworkExtension.NETunnelProviderRoutingMethodSourceApplication, 2)

            self.assertIsInstance(NetworkExtension.NETunnelProviderErrorDomain, unicode)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertArgIsBlock(NetworkExtension.NETunnelProvider.handleAppMessage_completionHandler_, 1, b'v@')
            self.assertArgIsBlock(NetworkExtension.NETunnelProvider.setTunnelNetworkSettings_completionHandler_, 1, b'v@')
            self.assertResultIsBOOL(NetworkExtension.NETunnelProvider.reasserting)
            self.assertArgIsBOOL(NetworkExtension.NETunnelProvider.setReasserting_, 0)


if __name__ == "__main__":
    main()
