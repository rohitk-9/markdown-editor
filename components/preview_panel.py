import tempfile
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex

class PreviewPanel(BoxLayout):
    html_content = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Button to open preview in browser
        self.open_in_browser_btn = Button(
            text="Open in Browser",
            size_hint=(1, None),
            height=40,
            background_color=get_color_from_hex("#00BCD4"),
            color=get_color_from_hex("#000000")
        )
        self.open_in_browser_btn.bind(on_release=self.open_in_browser)

        # Add only the button to the layout
        self.add_widget(self.open_in_browser_btn)

    def open_in_browser(self, *args):
        if not self.html_content.strip():
            return  # Nothing to show

        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding='utf-8') as temp_file:
            temp_file.write(self.html_content)
            temp_file.flush()
            webbrowser.open(f'file://{temp_file.name}')
