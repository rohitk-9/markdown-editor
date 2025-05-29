from kivy.uix.boxlayout import BoxLayout
from components.text_input import MarkdownInput
from components.toolbar import Toolbar
from models.markdown_parser import convert_markdown_to_html

class EditorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Pass content callback to toolbar
        self.editor = MarkdownInput(size_hint=(0.5, 1))
        self.toolbar = Toolbar(
            get_content_callback=lambda: self.editor.markdown_text,
            set_content_callback=self.set_editor_content
        )
        self.add_widget(self.toolbar)

        # Horizontal layout for editor and preview area
        body = BoxLayout(orientation='horizontal')
        body.add_widget(self.editor)

        # Optionally: Add preview panel here
        # body.add_widget(self.preview)

        self.add_widget(body)

        # Bind markdown text change to update preview
        self.editor.bind(markdown_text=self.on_markdown_text_change)

    def on_markdown_text_change(self, instance, text):
        html = convert_markdown_to_html(text)
        self.toolbar.set_html_content(html)

    def set_editor_content(self, new_text):
        self.editor.text = new_text