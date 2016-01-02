
from PyObjCTools.TestSupport import *
from LaunchServices import *

class TestUTCoreTypes (TestCase):
    def testConstants(self):
        self.assertIsInstance(kUTTypeItem, unicode)
        self.assertIsInstance(kUTTypeContent, unicode)
        self.assertIsInstance(kUTTypeCompositeContent, unicode)
        self.assertIsInstance(kUTTypeApplication, unicode)
        self.assertIsInstance(kUTTypeMessage, unicode)
        self.assertIsInstance(kUTTypeContact, unicode)
        self.assertIsInstance(kUTTypeArchive, unicode)
        self.assertIsInstance(kUTTypeDiskImage, unicode)
        self.assertIsInstance(kUTTypeData, unicode)
        self.assertIsInstance(kUTTypeDirectory, unicode)
        self.assertIsInstance(kUTTypeResolvable, unicode)
        self.assertIsInstance(kUTTypeSymLink, unicode)
        self.assertIsInstance(kUTTypeMountPoint, unicode)
        self.assertIsInstance(kUTTypeAliasFile, unicode)
        self.assertIsInstance(kUTTypeAliasRecord, unicode)
        self.assertIsInstance(kUTTypeURL, unicode)
        self.assertIsInstance(kUTTypeFileURL, unicode)
        self.assertIsInstance(kUTTypeText, unicode)
        self.assertIsInstance(kUTTypePlainText, unicode)
        self.assertIsInstance(kUTTypeUTF8PlainText, unicode)
        self.assertIsInstance(kUTTypeUTF16ExternalPlainText, unicode)
        self.assertIsInstance(kUTTypeUTF16PlainText, unicode)
        self.assertIsInstance(kUTTypeRTF, unicode)
        self.assertIsInstance(kUTTypeHTML, unicode)
        self.assertIsInstance(kUTTypeXML, unicode)
        self.assertIsInstance(kUTTypeSourceCode, unicode)
        self.assertIsInstance(kUTTypeCSource, unicode)
        self.assertIsInstance(kUTTypeObjectiveCSource, unicode)
        self.assertIsInstance(kUTTypeCPlusPlusSource, unicode)
        self.assertIsInstance(kUTTypeObjectiveCPlusPlusSource, unicode)
        self.assertIsInstance(kUTTypeCHeader, unicode)
        self.assertIsInstance(kUTTypeCPlusPlusHeader, unicode)
        self.assertIsInstance(kUTTypeJavaSource, unicode)
        self.assertIsInstance(kUTTypePDF, unicode)
        self.assertIsInstance(kUTTypeRTFD, unicode)
        self.assertIsInstance(kUTTypeFlatRTFD, unicode)
        self.assertIsInstance(kUTTypeTXNTextAndMultimediaData, unicode)
        self.assertIsInstance(kUTTypeWebArchive, unicode)
        self.assertIsInstance(kUTTypeImage, unicode)
        self.assertIsInstance(kUTTypeJPEG, unicode)
        self.assertIsInstance(kUTTypeJPEG2000, unicode)
        self.assertIsInstance(kUTTypeTIFF, unicode)
        self.assertIsInstance(kUTTypePICT, unicode)
        self.assertIsInstance(kUTTypeGIF, unicode)
        self.assertIsInstance(kUTTypePNG, unicode)
        self.assertIsInstance(kUTTypeQuickTimeImage, unicode)
        self.assertIsInstance(kUTTypeAppleICNS, unicode)
        self.assertIsInstance(kUTTypeBMP, unicode)
        self.assertIsInstance(kUTTypeICO, unicode)
        self.assertIsInstance(kUTTypeAudiovisualContent, unicode)
        self.assertIsInstance(kUTTypeMovie, unicode)
        self.assertIsInstance(kUTTypeVideo, unicode)
        self.assertIsInstance(kUTTypeAudio, unicode)
        self.assertIsInstance(kUTTypeQuickTimeMovie, unicode)
        self.assertIsInstance(kUTTypeMPEG, unicode)
        self.assertIsInstance(kUTTypeMPEG4, unicode)
        self.assertIsInstance(kUTTypeMP3, unicode)
        self.assertIsInstance(kUTTypeMPEG4Audio, unicode)
        self.assertIsInstance(kUTTypeAppleProtectedMPEG4Audio, unicode)
        self.assertIsInstance(kUTTypeFolder, unicode)
        self.assertIsInstance(kUTTypeVolume, unicode)
        self.assertIsInstance(kUTTypePackage, unicode)
        self.assertIsInstance(kUTTypeBundle, unicode)
        self.assertIsInstance(kUTTypeFramework, unicode)
        self.assertIsInstance(kUTTypeApplicationBundle, unicode)
        self.assertIsInstance(kUTTypeApplicationFile, unicode)
        self.assertIsInstance(kUTTypeVCard, unicode)
        self.assertIsInstance(kUTTypeInkText, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kUTTypeURLBookmarkData, unicode)
        self.assertIsInstance(kUTTypeDelimitedText, unicode)
        self.assertIsInstance(kUTTypeCommaSeparatedText, unicode)
        self.assertIsInstance(kUTTypeTabSeparatedText, unicode)
        self.assertIsInstance(kUTTypeUTF8TabSeparatedText, unicode)
        self.assertIsInstance(kUTTypeAssemblyLanguageSource, unicode)
        self.assertIsInstance(kUTTypeScript, unicode)
        self.assertIsInstance(kUTTypeAppleScript, unicode)
        self.assertIsInstance(kUTTypeOSAScript, unicode)
        self.assertIsInstance(kUTTypeOSAScriptBundle, unicode)
        self.assertIsInstance(kUTTypeJavaScript, unicode)
        self.assertIsInstance(kUTTypeShellScript, unicode)
        self.assertIsInstance(kUTTypePerlScript, unicode)
        self.assertIsInstance(kUTTypePythonScript, unicode)
        self.assertIsInstance(kUTTypeRubyScript, unicode)
        self.assertIsInstance(kUTTypePHPScript, unicode)
        self.assertIsInstance(kUTTypeJSON, unicode)
        self.assertIsInstance(kUTTypePropertyList, unicode)
        self.assertIsInstance(kUTTypeXMLPropertyList, unicode)
        self.assertIsInstance(kUTTypeBinaryPropertyList, unicode)
        self.assertIsInstance(kUTTypeRawImage, unicode)
        self.assertIsInstance(kUTTypeScalableVectorGraphics, unicode)
        self.assertIsInstance(kUTTypeMPEG2Video, unicode)
        self.assertIsInstance(kUTTypeMPEG2TransportStream, unicode)
        self.assertIsInstance(kUTTypeAppleProtectedMPEG4Video, unicode)
        self.assertIsInstance(kUTTypeAVIMovie, unicode)
        self.assertIsInstance(kUTTypeAudioInterchangeFileFormat, unicode)
        self.assertIsInstance(kUTTypeWaveformAudio, unicode)
        self.assertIsInstance(kUTTypeMIDIAudio, unicode)
        self.assertIsInstance(kUTTypePlaylist, unicode)
        self.assertIsInstance(kUTTypeM3UPlaylist, unicode)
        self.assertIsInstance(kUTTypePluginBundle, unicode)
        self.assertIsInstance(kUTTypeSpotlightImporter, unicode)
        self.assertIsInstance(kUTTypeQuickLookGenerator, unicode)
        self.assertIsInstance(kUTTypeXPCService, unicode)
        self.assertIsInstance(kUTTypeUnixExecutable, unicode)
        self.assertIsInstance(kUTTypeWindowsExecutable, unicode)
        self.assertIsInstance(kUTTypeJavaClass, unicode)
        self.assertIsInstance(kUTTypeJavaArchive, unicode)
        self.assertIsInstance(kUTTypeSystemPreferencesPane, unicode)
        self.assertIsInstance(kUTTypeGNUZipArchive, unicode)
        self.assertIsInstance(kUTTypeBzip2Archive, unicode)
        self.assertIsInstance(kUTTypeZipArchive, unicode)
        self.assertIsInstance(kUTTypeSpreadsheet, unicode)
        self.assertIsInstance(kUTTypePresentation, unicode)
        self.assertIsInstance(kUTTypeToDoItem, unicode)
        self.assertIsInstance(kUTTypeCalendarEvent, unicode)
        self.assertIsInstance(kUTTypeEmailMessage, unicode)
        self.assertIsInstance(kUTTypeInternetLocation, unicode)
        self.assertIsInstance(kUTTypeFont, unicode)
        self.assertIsInstance(kUTTypeBookmark, unicode)
        self.assertIsInstance(kUTType3DContent, unicode)
        self.assertIsInstance(kUTTypePKCS12, unicode)
        self.assertIsInstance(kUTTypeX509Certificate, unicode)
        self.assertIsInstance(kUTTypeElectronicPublication, unicode)
        self.assertIsInstance(kUTTypeLog, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(kUTTypeSwiftSource, unicode)

if __name__ == "__main__":
    main()
