import bleach

from io import StringIO
from html import escape

from .base import Widget


class Label(Widget):
    """A text label.

    Args:
        text (str): Text of the label.
        html (str): Text with html markup.
        id (str): An identifier for this widget.
        style (:obj:`Style`): An optional style object. If no style is provided then
            a new one will be created for the widget.
        factory (:obj:`module`): A python module that is capable to return a
            implementation of this class with the same name. (optional; normally not needed)
    """

    ALLOWED_TAGS = ['a', 'b', 'em', 'i', 'span', 'strong']
    ALLOWED_ATTRIBUTES = {'a': ['href', 'title'], 'span': ['style']}
    ALLOWED_STYLES = ['color', 'font-weight', 'font-family', 'font-size']

    def __init__(self, text=None, html=None, id=None, style=None, factory=None):
        super().__init__(id=id, style=style, factory=factory)

        self._html = ''

        # Create a platform specific implementation of a Label
        self._impl = self.factory.Label(interface=self)

        if text and html:
            raise ValueError('Must give either text or html')

        if text:
            self.text = text
        elif html:
            self.html = html

    @property
    def text(self):
        """The text displayed by the label.

        Returns:
            The text displayed by the label. All html attributes are stripped.
        """
        return bleach.clean(
            self._html,
            tags=[],
            attributes={},
            styles=[],
            protocols=[],
            strip=True
        )

    @text.setter
    def text(self, value):
        if value is None:
            self._html = ''
        else:
            self._html = escape(value)
            self._impl.set_html(self._html)

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):

        if value is None:
            self._html = ''
        else:
            self._html = bleach.clean(
                str(value),
                tags=self.ALLOWED_TAGS,
                attributes=self.ALLOWED_ATTRIBUTES,
                styles=self.ALLOWED_STYLES,
                strip=True
            )
            self._impl.set_html(value)
