import os
import subprocess

from utils import format_filename


class Printer:
    def __init__(self, print_folder):
        self.print_folder = print_folder
        self.create_print_folder()

    def create_print_folder(self):
        if not os.path.exists(self.print_folder):
            os.mkdir(self.print_folder)

    def print(self, file_name, file_content):
        new_file_name = format_filename(file_name)
        full_file_path = os.path.join(self.print_folder, new_file_name)

        # Save file content to a file
        with open(full_file_path, "wb") as file:
            file.write(file_content)

        # Print file (option "-r" specifies that the file will be deleted after being submitted
        print("Print file {}".format(file_name))
        subprocess.Popen(["/usr/bin/lpr", full_file_path, "-r"])
