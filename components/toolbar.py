import os
import time
import tempfile
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


class Toolbar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.spacing = 10
        self.padding = [10, 5]

        self.preview_button = Button(
            text="Open Preview in Browser",
            size_hint=(None, 1),
            width=220,
            background_color=get_color_from_hex("#00BCD4"),
            color=get_color_from_hex("#000000")
        )
        self.preview_button.bind(on_release=self.open_preview_in_browser)
        self.add_widget(self.preview_button)

        self.html_content = ""

        # Define and ensure preview directory
        self.preview_dir = os.path.join(tempfile.gettempdir(), "markdown_previews")
        os.makedirs(self.preview_dir, exist_ok=True)

        # Clean up old previews on start
        self.cleanup_old_previews()

    def set_html_content(self, html: str):
        self.html_content = html

    def open_preview_in_browser(self, *args):
        if not self.html_content.strip():
            return

        self.cleanup_old_previews()  # Optional: also clean before each render

        styled_html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Markdown Preview</title>
            <link rel="stylesheet"
                  href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
            <script>hljs.highlightAll();</script>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #1e1e1e;
                    color: #d4d4d4;
                    margin: 40px auto;
                    max-width: 800px;
                    padding: 0 20px;
                    line-height: 1.6;
                }}
                h1, h2, h3, h4 {{
                    color: #ffffff;
                    border-bottom: 1px solid #444;
                    padding-bottom: 4px;
                }}
                pre {{
                    background: #282c34;
                    border-radius: 5px;
                    overflow-x: auto;
                    padding: 10px;
                }}
                code {{
                    font-family: monospace;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin-top: 1em;
                    background-color: #2a2a2a;
                }}
                th, td {{
                    border: 1px solid #444;
                    padding: 8px;
                }}
                blockquote {{
                    border-left: 4px solid #00bcd4;
                    padding-left: 10px;
                    color: #aaa;
                    background-color: #252525;
                }}
            </style>
        </head>
        <body>
            {self.html_content}
        </body>
        </html>
        """

        timestamp = int(time.time() * 1000)
        file_path = os.path.join(self.preview_dir, f"preview_{timestamp}.html")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(styled_html)

        webbrowser.open(f'file://{file_path}')

    def cleanup_old_previews(self, age_limit_minutes=1):
        """Delete preview files older than `age_limit_minutes` from the preview folder."""
        now = time.time()
        for filename in os.listdir(self.preview_dir):
            file_path = os.path.join(self.preview_dir, filename)
            if os.path.isfile(file_path):
                file_age_seconds = now - os.path.getmtime(file_path)
                if file_age_seconds > age_limit_minutes * 60:
                    try:
                        os.remove(file_path)
                    except Exception as e:
                        print(f"Failed to delete {file_path}: {e}")
