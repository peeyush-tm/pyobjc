from PyObjCTools.TestSupport import *
import objc

import SceneKit

try:
    unicode
except NameError:
    unicode = str

class TestSCNParametricGeometry (TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNChamferModeBoth, 0)
        self.assertEqual(SceneKit.SCNChamferModeFront, 1)
        self.assertEqual(SceneKit.SCNChamferModeBack, 2)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNSphere.isGeodesic)
        self.assertArgIsBOOL(SceneKit.SCNSphere.setGeodesic_, 0)

        self.assertResultIsBOOL(SceneKit.SCNText.isWrapped)
        self.assertArgIsBOOL(SceneKit.SCNText.setWrapped_, 0)


if __name__ == "__main__":
    main()
