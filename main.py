                                                            # THESE COMMENTS ARE FOR THOSE WHO ARE LEARNING KIVY
from kivy.app import App                                    # Base class for application
from kivy.uix.boxlayout import BoxLayout                    # layout manager that arranges children in rows and columns
from kivy.core.window import Window                         # used to set window properties (like size or keyboard shortcut)
from kivy.utils import platform                             # help to set platform specific decision, crucial for cross platform support
from kivy.uix.textinput import TextInput


class RootWidget(BoxLayout):                                # creating root layout 
    def __init__(self, **kwargs):                           # This is temporary code    
        super().__init__(**kwargs)                          # this is used so that the appication stays on start
        self.orientation = 'vertical'                       # without it , it will be closing due no widget loaded
        self.text_input = TextInput(                        # to see it replace the whole def __init__ fuction with pass (i.e line 10 - 18)
            text="## Hello Markdown\n\nStart typing...",
            multiline=True,
            font_size=18,
        )
        self.add_widget(self.text_input)


class MarkdownEditorApp(App):
    def build(self):
        self.title = "Markdown Editor"
        if platform in ('win', 'linux', 'macosx'):
            Window.size = (1000, 600)
        return RootWidget()


if __name__ == '__main__':
    MarkdownEditorApp().run()