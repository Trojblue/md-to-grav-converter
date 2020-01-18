from typing import List
import re
import os.path

DEFAULT_PAGE_TYPE = "itm.zh"
DEFAULT_PATH = os.path.join(os.path.dirname(os.getcwd()), "outputs")  #
DEFAULT_YAML_PATH = "temp.yaml"


class Converter():
    """
    ===Public Attributes===
    md_path      path of original md file
    yaml_path    path of the temporary yaml file

    output_path  all result folders will be placed in this folder
    folder_name  name for the output folder
    page_type    md file in ./folder_name/ will be named as <page_type>.md

    md           raw content of original md file
    """

    def __init__(self, md_path: str, folder_name: str):
        """
        md_path: path of original md file
        folder_name: name for the output folder
        """
        self.md_path = md_path
        self.folder_name = folder_name
        self.set_page_type(DEFAULT_PAGE_TYPE)
        self.set_output_path(DEFAULT_PATH)
        self.set_yaml_path(DEFAULT_YAML_PATH)

        # self.read_md()


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
    def set_page_type(self, page_type: str):
        self.page_type = page_type

    def set_output_path(self, path: str):
        self.output_path = path

    def set_yaml_path(self, path: str):
        self.yaml_path = path

    def __repr__(self):
        return " md_path: %s \n yaml_path: %s \n output_path: %s \n folder_name: %s \n page_type: %s \n" % \
               (self.md_path, self.yaml_path, self.output_path, self.folder_name, self.page_type)
