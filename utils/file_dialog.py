import os
from kivy.utils import platform

def open_file_dialog(filetypes=(("Markdown", "*.md"), ("Text", "*.txt"), ("HTML", "*.html"))):
    """
    Open a file open dialog appropriate for the platform and return the selected path.
    """
    try:
        if platform in ("win", "linux", "macosx"):
            return _desktop_open_file_dialog(filetypes)
        elif platform == "android":
            return _android_open_file_dialog()
        elif platform == "ios":
            return _ios_open_file_dialog()
        else:
            print("Unsupported platform.")
            return None
    except Exception as e:
        print(f"Error during file dialog: {e}")
        return None

def _desktop_open_file_dialog(filetypes):
    try:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        root = Tk()
        root.withdraw()  # Hide the root window
        path = askopenfilename(defaultextension=".md",filetypes=filetypes)
        root.destroy()
        return path
    except ImportError:
        print("tkinter not available on this platform.")
        return None

def _android_open_file_dialog():
    from plyer import filechooser
    result = filechooser.open_file(title="Open Markdown File")
    if result:
        return result[0]
    return None

def _ios_open_file_dialog():
    # Placeholder: iOS needs native API integration or Kivy-iOS support.
    print("iOS file dialog not implemented.")
    return None

def get_save_path(extension=".md", default_filename="untitled.md"):
    """
    Open a file save dialog appropriate for the platform and return the selected path.
    Optionally, specify a default filename for the save dialog.
    """
    try:
        if platform in ("win", "linux", "macosx"):
            return _desktop_save_dialog(extension, default_filename)
        elif platform == "android":
            return _android_save_dialog(default_filename)
        elif platform == "ios":
            return _ios_save_dialog()
        else:
            print("Unsupported platform.")
            return None
    except Exception as e:
        print(f"Error during file dialog: {e}")
        return None

# Desktop save dialog with default filename support
def _desktop_save_dialog(extension, default_filename):
    try:
        from tkinter import Tk
        from tkinter.filedialog import asksaveasfilename

        root = Tk()
        root.withdraw()  # Hide the root window
        filetypes = [
            ("Markdown files", "*.md"),
            ("Text files", "*.txt"),
            ("HTML files", "*.html"),
            ("All files", "*.*")
        ]
        
        # Use default filename if provided, otherwise set to empty string
        filename = default_filename if default_filename else "untitled.md"
        
        # Prefill with the provided default filename
        path = asksaveasfilename(defaultextension=extension, filetypes=filetypes, initialfile=filename)
        root.destroy()
        return path
    except ImportError:
        print("tkinter not available on this platform.")
        return None

def _android_save_dialog(default_filename):
    from plyer import filechooser
    result = filechooser.save_file(title="Save Markdown File", default_filename=default_filename)
    if result:
        return result[0]
    return None

def _ios_save_dialog():
    # Placeholder: iOS needs native API integration or Kivy-iOS support.
    print("iOS file dialog not implemented.")
    return None
