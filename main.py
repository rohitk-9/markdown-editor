# main.py
from kivy.app import App
from screens.editor_screen import EditorScreen

class MarkdownEditorApp(App):
    def build(self):
        return EditorScreen()

if __name__ == "__main__":
    MarkdownEditorApp().run()
