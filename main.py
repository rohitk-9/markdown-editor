# THESE COMMENTS ARE FOR THOSE WHO ARE LEARNING KIVY
from kivy.app import App                                    # Base class for application
from kivy.core.window import Window                         # Used to set window properties (like size or keyboard shortcut)
from kivy.utils import platform                             # Help to set platform specific decision, crucial for cross platform support

from screens.editor_screen import EditorScreen              # Import the modular EditorScreen (the main UI screen)


class MarkdownEditorApp(App):
    def build(self):
        self.title = "Markdown Editor"
        
        # Set window size for desktop platforms
        if platform in ('win', 'linux', 'macosx'):
            Window.size = (1000, 600)
        
        # Return the main editor screen as root widget
        return EditorScreen()


if __name__ == '__main__':
    MarkdownEditorApp().run()
