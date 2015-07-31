from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import NotificationCenter

    class TestNCWidgetProvidingHelper (NotificationCenter.NSObject):
        def widgetPerformUpdateWithCompletionHandler_(self, handler): pass
        def widgetMarginInsetsForProposedMarginInsets_(self, insets): return insets
        def widgetAllowsEditing(self): return True


    class TestNCWidgetProviding (TestCase):
        @min_os_level('10.10')
        def testConstants10_10(self):
            self.assertEqual(NotificationCenter.NCUpdateResultNewData, 0)
            self.assertEqual(NotificationCenter.NCUpdateResultNoData, 1)
            self.assertEqual(NotificationCenter.NCUpdateResultFailed, 2)

        @min_os_level('10.10')
        def testClasses10_10(self):
            objc.protocolNamed('NCWidgetProviding')

            self.assertArgIsBlock(TestNCWidgetProvidingHelper.widgetPerformUpdateWithCompletionHandler_, 0, b'v' + objc._C_NSUInteger)
            self.assertResultHasType(TestNCWidgetProvidingHelper.widgetMarginInsetsForProposedMarginInsets_, NotificationCenter.NSEdgeInsets.__typestr__)
            self.assertArgHasType(TestNCWidgetProvidingHelper.widgetMarginInsetsForProposedMarginInsets_, 0, NotificationCenter.NSEdgeInsets.__typestr__)
            self.assertResultIsBOOL(TestNCWidgetProvidingHelper.widgetAllowsEditing)



if __name__ == "__main__":
    main()
