# editor_screen.py
from kivy.uix.boxlayout import BoxLayout
from ..components.text_input import MarkdownTextInput


class EditorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='horizontal', **kwargs)

        self.editor = MarkdownTextInput()
        self.add_widget(self.editor)
