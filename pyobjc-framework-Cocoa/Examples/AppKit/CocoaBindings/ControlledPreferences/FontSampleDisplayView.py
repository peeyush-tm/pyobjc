#
#  FontSampleDisplayView.py
#  ControlledPreferences
#
#  Converted by u.fiedler on 04.02.05.
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from objc import super
from Cocoa import NSView, NSUserDefaultsController, NSUnarchiver
from Cocoa import NSDrawLightBezel, NSRectFill, NSInsetRect
from Cocoa import NSFontAttributeName, NSAttributedString, NSFont
from Cocoa import NSMakePoint, NSNotificationCenter, NSUserDefaultsDidChangeNotification
from PyObjCTools.KeyValueCoding import getKey

class FontSampleDisplayView(NSView):
    """
    Display WordOfTheDay with the preferred font and color
    """
    def drawRect_(self, rect):
        defaults = NSUserDefaultsController.sharedUserDefaultsController().values()
        favoriteColor = NSUnarchiver.unarchiveObjectWithData_(getKey(defaults, 'FavoriteColor'))
        fontName = getKey(defaults, 'FontName')
        fontSize = getKey(defaults, 'FontSize')
        favoriteFont = NSFont.fontWithName_size_(fontName, fontSize)
        wordOfTheDay = getKey(defaults, 'WordOfTheDay')

        # Do the actual drawing
        myBounds = self.bounds() # = (x, y), (bw, bh)
        NSDrawLightBezel(myBounds, myBounds)
        favoriteColor.set()
        NSRectFill(NSInsetRect(myBounds, 2, 2))
        attrsDictionary = {NSFontAttributeName: favoriteFont}
        attrString = NSAttributedString.alloc().initWithString_attributes_(wordOfTheDay, attrsDictionary)
        attrSize = attrString.size() # = (bw, bh)
        attrString.drawAtPoint_(
            NSMakePoint(
                (attrSize.width / -2) + (myBounds.size.width / 2),
                (attrSize.height / -2) + (myBounds.size.height / 2),
            ),
        )

    def initWithFrame_(self, frameRect):
        self = super(FontSampleDisplayView, self).initWithFrame_(frameRect)
        dnc = NSNotificationCenter.defaultCenter()
        dnc.addObserver_selector_name_object_(self, "redisplay:", NSUserDefaultsDidChangeNotification, None)
        return self

    def redisplay_(self, sender):
        self.setNeedsDisplay_(True)
