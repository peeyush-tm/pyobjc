from PyObjCTools.TestSupport import *
import objc
import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2**32:
    import Contacts

    class TestCNError (TestCase):
        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(Contacts.CNErrorDomain, unicode)

            self.assertEqual(Contacts.CNErrorCodeCommunicationError, 1)
            self.assertEqual(Contacts.CNErrorCodeDataAccessError, 2)
            self.assertEqual(Contacts.CNErrorCodeAuthorizationDenied, 100)
            self.assertEqual(Contacts.CNErrorCodeRecordDoesNotExist, 200)
            self.assertEqual(Contacts.CNErrorCodeInsertedRecordAlreadyExists, 201)
            self.assertEqual(Contacts.CNErrorCodeContainmentCycle, 202)
            self.assertEqual(Contacts.CNErrorCodeContainmentScope, 203)
            self.assertEqual(Contacts.CNErrorCodeParentRecordDoesNotExist, 204)
            self.assertEqual(Contacts.CNErrorCodeValidationMultipleErrors, 300)
            self.assertEqual(Contacts.CNErrorCodeValidationTypeMismatch, 301)
            self.assertEqual(Contacts.CNErrorCodeValidationConfigurationError, 302)
            self.assertEqual(Contacts.CNErrorCodePredicateInvalid, 400)
            self.assertEqual(Contacts.CNErrorCodePolicyViolation, 500)

            self.assertIsInstance(Contacts.CNErrorUserInfoAffectedRecordsKey, unicode)
            self.assertIsInstance(Contacts.CNErrorUserInfoAffectedRecordIdentifiersKey, unicode)
            self.assertIsInstance(Contacts.CNErrorUserInfoValidationErrorsKey, unicode)
            self.assertIsInstance(Contacts.CNErrorUserInfoKeyPathsKey, unicode)


if __name__ == "__main__":
    main()
