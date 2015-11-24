from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str


class TestAVAudioUnit (TestCase):
    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBlock(AVFoundation.AVAudioUnit.instantiateWithComponentDescription_options_completionHandler_, 2, b'v@@')

        self.assertResulsIsBOOL(AVFoundation.AVAudioUnit.loadAudioUnitPresetAtURL_error_)
        self.assertArgIsOut(AVFoundation.AVAudioUnit.loadAudioUnitPresetAtURL_error_, 1)

if __name__ == "__main__":
    main()
