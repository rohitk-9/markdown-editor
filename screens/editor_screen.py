# screens/editor_screen.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from components.preview_panel import PreviewButton
from kivy.utils import get_color_from_hex


class EditorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.markdown_input = TextInput(

            size_hint_y=0.9,

            multiline = True,
        font_size = 18,
        padding = [10, 10, 10, 10],
        cursor_color = get_color_from_hex("#00BCD4") ,
        background_color = get_color_from_hex("#1e1e1e"),
        foreground_color = get_color_from_hex("#ffffff"),
        hint_text = "Start writing your markdonw text here ..."
        )

        self.preview_button = PreviewButton(self.get_text, size_hint_y=0.1)
        self.add_widget(self.markdown_input)
        self.add_widget(self.preview_button)

    def get_text(self):
        return self.markdown_input.text
