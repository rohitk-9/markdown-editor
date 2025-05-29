# models/file_manager.py
import os
from utils.file_dialog import open_file_dialog, get_save_path  # Ensure this is correct

class FileManager:
    def open_file(self, filetypes=(("Markdown", "*.md"), ("Text", "*.txt"), ("HTML", "*.html"))):
        """Open a file and return its content along with the file path."""
        file_path = open_file_dialog(filetypes)
        if file_path and os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content, file_path
        return None, None

    def save_file(self, file_path, content):
        """Save content to the specified file path."""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True  # Indicating that saving was successful
        except Exception as e:
            print(f"Error saving file: {e}")
            return False  # Indicating failure

    def save_file_as(self, content, filetypes=(("Markdown", "*.md"), ("Text", "*.txt"), ("HTML", "*.html"))):
        """Trigger the 'Save As' dialog and save the content to the selected path."""
        file_path = get_save_path(filetypes)
        if file_path:  # If a file path was returned (i.e., user selected a location)
            return self.save_file(file_path, content), file_path  # Save and return status and file path
        return False, None  # If the user canceled, return False
