#
#  FontNameToDisplayNameTransformer.py
#  ControlledPreferences
#
#  Converted by u.fiedler on 04.02.05.
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Cocoa import NSValueTransformer, NSString, NSFont

class FontNameToDisplayNameTransformer(NSValueTransformer):
    """
    Takes as input the fontName of a font as stored in user defaults,
    returns the displayed font name of the font to show to the user.
    """
    @classmethod
    def transformedValueClass(cls):
        return NSString

    @classmethod
    def allowsReverseTransformation(cls):
        return False

    def transformedValue_(self, aValue):
        font = NSFont.fontWithName_size_(aValue, 12)
        return font.displayName()
