
from PyObjCTools.TestSupport import *
import objc

import SceneKit

try:
    unicode
except NameError:
    unicode = str

class TestSCNMorpher (TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNMorpherCalculationModeNormalized, 0)
        self.assertEqual(SceneKit.SCNMorpherCalculationModeAdditive, 1)

if __name__ == "__main__":
    main()
