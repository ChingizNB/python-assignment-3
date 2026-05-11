import os

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def check_file(self):
        if os.path.exists(self.file_path):
            print(f"File found: {self.file_path}")
            return True
        print(f"Error: {self.file_path} not found.")
        return False

    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Folder '{folder}' created.")