import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBAdvertisementData (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(CoreBluetooth.CBErrorDomain, unicode)
        self.assertIsInstance(CoreBluetooth.CBATTErrorDomain, unicode)

        self.assertEqual(CoreBluetooth.CBErrorUnknown, 0)
        self.assertEqual(CoreBluetooth.CBErrorInvalidParameters, 1)
        self.assertEqual(CoreBluetooth.CBErrorInvalidHandle, 2)
        self.assertEqual(CoreBluetooth.CBErrorNotConnected, 3)
        self.assertEqual(CoreBluetooth.CBErrorOutOfSpace, 4)
        self.assertEqual(CoreBluetooth.CBErrorOperationCancelled, 5)
        self.assertEqual(CoreBluetooth.CBErrorConnectionTimeout, 6)
        self.assertEqual(CoreBluetooth.CBErrorPeripheralDisconnected, 7)
        self.assertEqual(CoreBluetooth.CBErrorUUIDNotAllowed, 8)
        self.assertEqual(CoreBluetooth.CBErrorAlreadyAdvertising, 9)

        self.assertEqual(CoreBluetooth.CBATTErrorSuccess, 0x00)
        self.assertEqual(CoreBluetooth.CBATTErrorInvalidHandle, 0x01)
        self.assertEqual(CoreBluetooth.CBATTErrorReadNotPermitted, 0x02)
        self.assertEqual(CoreBluetooth.CBATTErrorWriteNotPermitted, 0x03)
        self.assertEqual(CoreBluetooth.CBATTErrorInvalidPdu, 0x04)
        self.assertEqual(CoreBluetooth.CBATTErrorInsufficientAuthentication, 0x05)
        self.assertEqual(CoreBluetooth.CBATTErrorRequestNotSupported, 0x06)
        self.assertEqual(CoreBluetooth.CBATTErrorInvalidOffset, 0x07)
        self.assertEqual(CoreBluetooth.CBATTErrorInsufficientAuthorization, 0x08)
        self.assertEqual(CoreBluetooth.CBATTErrorPrepareQueueFull, 0x09)
        self.assertEqual(CoreBluetooth.CBATTErrorAttributeNotFound, 0x0A)
        self.assertEqual(CoreBluetooth.CBATTErrorAttributeNotLong, 0x0B)
        self.assertEqual(CoreBluetooth.CBATTErrorInsufficientEncryptionKeySize, 0x0C)
        self.assertEqual(CoreBluetooth.CBATTErrorInvalidAttributeValueLength, 0x0D)
        self.assertEqual(CoreBluetooth.CBATTErrorUnlikelyError, 0x0E)
        self.assertEqual(CoreBluetooth.CBATTErrorInsufficientEncryption, 0x0F)
        self.assertEqual(CoreBluetooth.CBATTErrorUnsupportedGroupType, 0x10)
        self.assertEqual(CoreBluetooth.CBATTErrorInsufficientResources, 0x11)

if __name__ == "__main__":
    main()
