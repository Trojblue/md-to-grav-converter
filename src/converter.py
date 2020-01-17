from typing import List
import re
import os

"""
Main class for conversion process
"""

DEFAULT_NAME = "itm.zh.md"  # name of the output markdown file
OUTPUT_PATH = os.path.join(os.path.dirname(os.getcwd()), "outputs") # /outputs
SAMPLE_FILE = os.path.join(os.path.dirname(os.getcwd()), "bin", "test.md") # /bin/test.md

class Converter():

    def __init__(self, path:str):
        """
        path: path of the markdown file to be processed
        """
        self._inputPath = path
        self.read_md()

    def read_md(self) -> None:
        """reads markdown file into a list of lines
        """
        try:
            input = open(self._inputPath, "r")
            lines = input.readlines()
            self._lines = lines
            print("--read_md test--")
            print("reading %s lines of markdown file; first line: %s"
                  % (len(self._lines), self._lines[0]))

        except FileNotFoundError:
            print("File not found!")

    def convert(self):
        pass

    # Additional functions
    def set_path(self, path:str):
        """set a new path for the markdown file to be processed
        """
        self._inputPath = path


