from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TextEditor(App):
    def build(self):
        root = BoxLayout(orientation='vertical') 
        return Label(text="Hello")
        TextInput = TextInput()
        root.add_widget(TextInput)


obj = TextEditor()
if __name__ == "__main__":
    obj.run()