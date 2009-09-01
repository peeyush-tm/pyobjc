from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSOperation (TestCase):
    def testConstants(self):
        self.assertEquals(NSOperationQueuePriorityVeryLow, -8)
        self.assertEquals(NSOperationQueuePriorityLow, -4)
        self.assertEquals(NSOperationQueuePriorityNormal, 0)
        self.assertEquals(NSOperationQueuePriorityHigh, 4)
        self.assertEquals(NSOperationQueuePriorityVeryHigh, 8)

        self.failUnless(isinstance(NSInvocationOperationVoidResultException, unicode))
        self.failUnless(isinstance(NSInvocationOperationCancelledException, unicode))

        self.assertEquals(NSOperationQueueDefaultMaxConcurrentOperationCount, -1)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSOperation.isCancelled)
        self.failUnlessResultIsBOOL(NSOperation.isExecuting)
        self.failUnlessResultIsBOOL(NSOperation.isFinished)
        self.failUnlessResultIsBOOL(NSOperation.isConcurrent)
        self.failUnlessResultIsBOOL(NSOperation.isReady)

        self.failUnlessResultIsBOOL(NSOperationQueue.isSuspended)
        self.failUnlessArgIsBOOL(NSOperationQueue.setSuspended_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBlock(NSOperation.completionBlock, 'v')
        self.failUnlessArgIsBlock(NSOperation.setCompletionBlock_, 0, 'v')

        self.failUnlessArgIsBlock(NSBlockOperation.blockOperationWithBlock_, 0, 'v')
        self.failUnlessArgIsBlock(NSBlockOperation.addExecutionBlock_, 0, 'v')

        self.failUnlessArgIsBOOL(NSOperationQueue.addOperations_waitUntilFinished_, 1)
        self.failUnlessArgIsBlock(NSOperationQueue.addOperationWithBlock_, 0, 'v')

if __name__ == "__main__":
    main()
