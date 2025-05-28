# screens/editor_screen.py

from kivy.uix.boxlayout import BoxLayout
from components.text_input import MarkdownInput
from components.toolbar import Toolbar
from models.markdown_parser import convert_markdown_to_html


class EditorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Toolbar on top
        self.toolbar = Toolbar()
        self.add_widget(self.toolbar)

        # Horizontal layout for editor and preview area
        body = BoxLayout(orientation='horizontal')

        self.editor = MarkdownInput(size_hint=(0.5, 1))
        body.add_widget(self.editor)

        # Placeholder PreviewPanel, if needed later
        # For now, only using browser preview
        # self.preview = PreviewPanel(size_hint=(0.5, 1))
        # body.add_widget(self.preview)

        self.add_widget(body)

        # Bind markdown text change
        self.editor.bind(markdown_text=self.on_markdown_text_change)

    def on_markdown_text_change(self, instance, text):
        html = convert_markdown_to_html(text)
        self.toolbar.set_html_content(html)
