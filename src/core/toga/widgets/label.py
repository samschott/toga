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

    def __init__(self, text=None, html=None, id=None, style=None, factory=None):
        super().__init__(id=id, style=style, factory=factory)

        self._html = ''
        self._text = ''

        # Create a platform specific implementation of a Label
        self._impl = self.factory.Label(interface=self)

        self.text = text
        self.html = html

    @property
    def text(self):
        """The text displayed by the label.

        Returns:
            The text displayed by the label.
        """
        return self._text

    @text.setter
    def text(self, value):
        if value is None:
            self._text = ''
        else:
            self._text = str(value)
            self._impl.set_text(value)

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, value):
        if value is None:
            self._html = ''
        else:
            self._html = str(value)
            self._impl.set_html(value)
