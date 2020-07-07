import toga
from toga.style import Pack
from toga.constants import COLUMN, RED, DARKGREY


class LabelDemoApp(toga.App):

    def startup(self):
        # Set up main window
        self.main_window = toga.MainWindow(title=self.name)

        url = 'https://toga.readthedocs.io/en/latest/'

        self.label0 = toga.Label(text='Plain text', style=Pack(color=RED))
        self.label1 = toga.Label(html='<i>Italic text</i>', style=Pack(color=DARKGREY))
        self.label2 = toga.Label(html='<a href="{0}">{0}</a>'.format(url))

        # Outermost box
        outer_box = toga.Box(
            children=[self.label0, self.label1, self.label2],
            style=Pack(
                flex=1,
                direction=COLUMN,
                padding=20,
                width=400,
                height=250
            )
        )

        # Add the content on the main window
        self.main_window.content = outer_box

        # Show the main window
        self.main_window.show()


def main():
    return LabelDemoApp('Label Demo', 'org.beeware.widgets.label')


if __name__ == '__main__':
    app = main()
    app.main_loop()
