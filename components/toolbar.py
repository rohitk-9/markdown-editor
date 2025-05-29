import os
import time
import tempfile
import webbrowser
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from models.file_manager import FileManager


class Toolbar(BoxLayout):
    def __init__(self, get_content_callback=None, set_content_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.spacing = 10
        self.padding = [10, 5]

        self.current_file_path = None

        self.get_content_callback = get_content_callback  # This should return the Markdown string to save
        self.set_content_callback = set_content_callback  # This should allow setting new content in the editor

        # Save Button
        self.save_button = Button(
            text="Save",
            size_hint=(None, 1),
            width=150,
            background_color=get_color_from_hex("#4CAF50"),
            color=get_color_from_hex("#FFFFFF")
        )
        self.save_button.bind(on_release=self.save_markdown)
        self.add_widget(self.save_button)

        # Save As Button
        self.save_as_button = Button(
            text="Save As",
            size_hint=(None, 1),
            width=150,
            background_color=get_color_from_hex("#FFC107"),
            color=get_color_from_hex("#FFFFFF")
        )
        self.save_as_button.bind(on_release=self.save_markdown_as)
        self.add_widget(self.save_as_button)

        # Open Button
        self.open_button = Button(
            text="Open",
            size_hint=(None, 1),
            width=150,
            background_color=get_color_from_hex("#2196F3"),
            color=get_color_from_hex("#FFFFFF")
        )
        self.open_button.bind(on_release=self.open_file)
        self.add_widget(self.open_button)

        # Preview Button
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

    
    
    def show_message(self, message):
        """Function to show a popup with the provided message."""
        content = BoxLayout(orientation='vertical')

        # Label now uses the dynamic message
        message_label = Label(text=message, size_hint=(None, None), size=(300, 100))
        content.add_widget(message_label)

        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50))
        close_button.bind(on_release=self.close_popup)
        content.add_widget(close_button)

        self.popup = Popup(
            title="Message",
            content=content,
            size_hint=(None, None),
            size=(400, 200),
            auto_dismiss=False
        )

        self.popup.open()

    def close_popup(self, instance):
        """Function to close the popup."""
        self.popup.dismiss() 
    
    
    
    
    
    def set_html_content(self, html: str):
        """Set the current HTML content for live preview."""
        self.html_content = html

    def save_markdown(self, *args):
        """Save to the current file if available."""
        if not self.get_content_callback:
            print("No content callback provided for saving.")
            return

        content = self.get_content_callback()
        if not content.strip():
            print("Nothing to save.")
            return

        if self.current_file_path:
            file_manager = FileManager()
            success = file_manager.save_file(self.current_file_path, content)
            if success:
                self.show_message("File saved successfully.")
            else:
                self.show_message("Failed to save file.")
            print("Saved" if success else "Save failed")
        else:
            # Fallback to Save As if no path exists yet
            self.save_markdown_as()

    def save_markdown_as(self, *args):
        """Prompt user to choose a file path to save content."""
        if not self.get_content_callback:
            print("No content callback provided for saving.")
            return
    
        content = self.get_content_callback()
        if not content.strip():
            print("Nothing to save.")
            return
    
        file_manager = FileManager()
        success, file_path = file_manager.save_file_as(content)
        if success:
            self.current_file_path = file_path
            print(f"Saved to {file_path}")
            self.show_message("File saved successfully.")
        else:
            print("Save As cancelled or failed.")
            self.show_message("Failed to save file.")


    def open_file(self, *args):
        """Triggered when 'Open' is pressed. Uses callback and FileManager to load content."""
        file_manager = FileManager()
        content, file_path = file_manager.open_file(filetypes=(("Markdown", "*.md"), ("Text", "*.txt"), ("HTML", "*.html")))
        if content:
            if self.set_content_callback:
                self.set_content_callback(content)
                self.current_file_path = file_path
            print(f"File '{file_path}' loaded successfully.")
        else:
            print("Failed to load file.")

    def open_preview_in_browser(self, *args):
        if not self.html_content.strip():
            return

        self.cleanup_old_previews()

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

    def cleanup_old_previews(self, age_limit_minutes=10):
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
