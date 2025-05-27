                                                            # THESE COMMENTS ARE FOR THOSE WHO ARE LEARNING KIVY
from kivy.app import App                                    # Base class for application
from kivy.uix.boxlayout import BoxLayout                    # layout manager that arranges children in rows and columns
from kivy.core.window import Window                         # used to set window properties (like size or keyboard shortcut)
from kivy.utils import platform                             # help to set platform specific decision, crucial for cross platform support
from components.text_input import MarkdownInput


class RootWidget(BoxLayout):                                # creating root layout 
    def __init__(self, **kwargs):                           
        super().__init__(**kwargs)                          
        self.orientation = 'vertical'                       
        
        self.markdown_input = MarkdownInput()               # displaying text_input from components
        self.add_widget(self.markdown_input)                


class MarkdownEditorApp(App):
    def build(self):
        self.title = "Markdown Editor"
        if platform in ('win', 'linux', 'macosx'):
            Window.size = (1000, 600)
        return RootWidget()


if __name__ == '__main__':
    MarkdownEditorApp().run()