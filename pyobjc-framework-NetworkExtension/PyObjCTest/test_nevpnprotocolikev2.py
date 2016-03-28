from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEVPNProtocolIKEv2 (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NEVPNIKEv2EncryptionAlgorithmDES, 1)
            self.assertEqual(NetworkExtension.NEVPNIKEv2EncryptionAlgorithm3DES, 2)
            self.assertEqual(NetworkExtension.NEVPNIKEv2EncryptionAlgorithmAES128, 3)
            self.assertEqual(NetworkExtension.NEVPNIKEv2EncryptionAlgorithmAES256, 4)
            self.assertEqual(NetworkExtension.NEVPNIKEv2EncryptionAlgorithmAES128GCM, 5)
            self.assertEqual(NetworkExtension.NEVPNIKEv2EncryptionAlgorithmAES256GCM, 6)

            self.assertEqual(NetworkExtension.NEVPNIKEv2IntegrityAlgorithmSHA96, 1)
            self.assertEqual(NetworkExtension.NEVPNIKEv2IntegrityAlgorithmSHA160, 2)
            self.assertEqual(NetworkExtension.NEVPNIKEv2IntegrityAlgorithmSHA256, 3)
            self.assertEqual(NetworkExtension.NEVPNIKEv2IntegrityAlgorithmSHA384, 4)
            self.assertEqual(NetworkExtension.NEVPNIKEv2IntegrityAlgorithmSHA512, 5)

            self.assertEqual(NetworkExtension.NEVPNIKEv2DeadPeerDetectionRateNone, 0)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DeadPeerDetectionRateLow, 1)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DeadPeerDetectionRateMedium, 2)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DeadPeerDetectionRateHigh, 3)

            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup0, 0)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup1, 1)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup2, 2)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup5, 5)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup14, 14)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup15, 15)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup16, 16)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup17, 17)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup18, 18)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup19, 19)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup20, 20)
            self.assertEqual(NetworkExtension.NEVPNIKEv2DiffieHellmanGroup21, 21)

            self.assertEqual(NetworkExtension.NEVPNIKEv2CertificateTypeRSA, 1)
            self.assertEqual(NetworkExtension.NEVPNIKEv2CertificateTypeECDSA256, 2)
            self.assertEqual(NetworkExtension.NEVPNIKEv2CertificateTypeECDSA384, 3)
            self.assertEqual(NetworkExtension.NEVPNIKEv2CertificateTypeECDSA521, 4)


        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.useConfigurationAttributeInternalIPSubnet)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.setUseConfigurationAttributeInternalIPSubnet_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.disableMOBIKE)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.setDisableMOBIKE_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.disableRedirect)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.setDisableRedirect_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.enablePFS)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.setEnablePFS_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.enableRevocationCheck)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.setEnableRevocationCheck_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.strictRevocationCheck)
            self.assertArgIsBOOL(NetworkExtension.NEVPNProtocolIKEv2.setStrictRevocationCheck_, 0)


if __name__ == "__main__":
    main()
