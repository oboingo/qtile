from libqtile import bar
from libqtile.widget.textbox import TextBox


class KeyChordWidget(TextBox):
    """A widget to display the current KeyChord status"""
    instances = []

    def __init__(self, text=" ", width=bar.CALCULATED, **config):
        super().__init__(text, width, **config)
        KeyChordWidget.instances.append(self)
