from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex

class MarkdownInput(TextInput):
    markdown_text = StringProperty("") 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = True
        self.font_size = 18
        self.padding = [10, 10, 10, 10]
        self.cursor_color = get_color_from_hex("#00BCD4") 
        self.background_color = get_color_from_hex("#1e1e1e")
        self.foreground_color = get_color_from_hex("#ffffff")
        self.hint_text = "Start writing your markdonw text here ..."

        self.bind(text=self.on_text_change)

    def on_text_change(self, instance, text):
        self.markdown_text = text   