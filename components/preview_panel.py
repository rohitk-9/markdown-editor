# components/preview_panel.py
from kivy.uix.button import Button
from models.markdown_parser import preview_markdown

class PreviewButton(Button):
    def __init__(self, get_text_callback, **kwargs):
        super().__init__(text="Live Preview", **kwargs)
        self.get_text_callback = get_text_callback
        self.on_press = self.show_preview

    def show_preview(self):
        text = self.get_text_callback()
        preview_markdown(text)
