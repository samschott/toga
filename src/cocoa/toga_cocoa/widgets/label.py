from travertino.size import at_least

from toga_cocoa.colors import native_color
from toga_cocoa.libs import (
    NSTextAlignment, NSTextView, NSColor, NSString, NSMutableAttributedString,
    NSColorSpace, NSUTF8StringEncoding
)

from rubicon.objc import at
from .base import Widget


def attributed_str_from_html(raw_html, font=None, color=None):
    """Converts html to a NSAttributed string using the system font family and color."""

    html_value = """
    <span style="font-family: '{0}'; font-size: {1}; color: {2}">
    {3}
    </span>
    """
    font_family = font.fontName if font else 'system-ui'
    font_size = font.pointSize if font else 13
    color = color or NSColor.labelColor
    c = color.colorUsingColorSpace(NSColorSpace.deviceRGBColorSpace)
    c_str = f'rgb({c.redComponent * 255},{c.blueComponent * 255},{c.greenComponent * 255})'
    html_value = html_value.format(font_family, font_size, c_str, raw_html)
    nsstring = NSString(at(html_value))
    data = nsstring.dataUsingEncoding(NSUTF8StringEncoding)
    attr_str = NSMutableAttributedString.alloc().initWithHTML(
        data,
        documentAttributes=None,
    )
    return attr_str


class Label(Widget):

    def create(self):
        self._color = None

        self.native = NSTextView.alloc().init()
        self.native.impl = self
        self.native.interface = self.interface

        self.native.drawsBackground = False
        self.native.editable = False
        self.native.selectable = True
        self.native.textContainer.lineFragmentPadding = 0

        self.native.bezeled = False

        # Add the layout constraints
        self.add_constraints()

    def set_alignment(self, value):
        self.native.alignment = NSTextAlignment(value)

    def set_color(self, value):

        if value:
            self._color = native_color(value)
        else:
            self._color = None

        # refresh the html with new color attribute
        self.set_html(self.interface.html)

    def set_font(self, value):

        if value:
            self.native.font = value._impl.native

    def set_html(self, value):

        if value:
            attr_str = attributed_str_from_html(value, self.native.font, self._color)
            self.native.textStorage.setAttributedString(attr_str)

        self.rehint()

    def rehint(self):
        # force layout
        self.native.layoutManager.glyphRangeForTextContainer(self.native.textContainer)
        # get layout rect
        rect = self.native.layoutManager.usedRectForTextContainer(self.native.textContainer)

        self.interface.intrinsic.width = at_least(rect.size.width)
        self.interface.intrinsic.height = rect.size.height
