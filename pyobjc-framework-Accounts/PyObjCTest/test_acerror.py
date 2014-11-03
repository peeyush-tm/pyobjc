import sys

if sys.maxsize > 2**32:
    from PyObjCTools.TestSupport import *
    import Accounts

    try:
        unicode
    except NameError:
        unicode = str

    class TestACError (TestCase):
        @min_os_level("10.9")
        def testConstants10_9(self):
            self.assertEqual(Accounts.ACErrorAccessDeniedByProtectionPolicy, 10)
            self.assertEqual(Accounts.ACErrorClientPermissionDenied, 9)
            self.assertEqual(Accounts.ACErrorCredentialNotFound, 11)
            self.assertEqual(Accounts.ACErrorFetchCredentialFailed, 12)
            self.assertEqual(Accounts.ACErrorInvalidClientBundleID, 16)
            self.assertEqual(Accounts.ACErrorRemoveCredentialFailed, 14)
            self.assertEqual(Accounts.ACErrorStoreCredentialFailed, 13)
            self.assertEqual(Accounts.ACErrorUpdatingNonexistentAccount, 15)

        @min_os_level("10.8")
        def testConstants(self):
            self.assertIsInstance(Accounts.ACErrorDomain, unicode)

            self.assertEqual(Accounts.ACErrorUnknown, 1)
            self.assertEqual(Accounts.ACErrorAccountMissingRequiredProperty, 2)
            self.assertEqual(Accounts.ACErrorAccountAuthenticationFailed, 3)
            self.assertEqual(Accounts.ACErrorAccountTypeInvalid, 4)
            self.assertEqual(Accounts.ACErrorAccountAlreadyExists, 5)
            self.assertEqual(Accounts.ACErrorAccountNotFound, 6)
            self.assertEqual(Accounts.ACErrorPermissionDenied, 7)
            self.assertEqual(Accounts.ACErrorAccessInfoInvalid, 8)

    if __name__ == "__main__":
        main()
