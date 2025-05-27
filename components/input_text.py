# components/text_input.py
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty

class MarkdownTextInput(TextInput):
    markdown_text = StringProperty("")  # for two-way binding

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = True
        self.font_size = 16
        self.cursor_color = (0, 0.5, 1, 1)
        self.hint_text = "Write your Markdown here..."
        self.bind(text=self.on_text_change)

    def on_text_change(self, instance, value):
        self.markdown_text = value