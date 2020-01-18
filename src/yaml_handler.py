import fileinput
from converter import Converter
from handler import Handler

"""
TODO:
- title
- media_order
- date
- taxonomy
- summary
"""

class YAMLHandler (Handler):
    """
    添加默认的yaml头文件
    """

    def __init__(self, converter: Converter):
        super().__init__(converter)  # todo: maybe wrong here
        self._yaml_dict = {}
        self.yaml_path = "./temp.yaml"


    def set_title(self):
        title = input("input the title:")
        self._yaml_dict["title"] = title

    def set_summary(self):
        summary = input("input the summary: leave [blank] to use title; type [N] to not use summary")
        if summary == "":
            summary = self._yaml_dict["title"]
        elif summary == "N" or summary == "n":
            self._yaml_dict['summary'] = {'enabled': '0'}
            return
        self._yaml_dict['summary'] = {'enabled': '1'}
        # todo: link handler to converter;
        # todo: handler has a queue of to-add arguments

    def set_media_order(self):
        """默认按时间顺序
        """
        pass

    def set_date(self):
        """今天, 或者根据markdown创建时间
        """
        pass

    def set_taxonomy(self, category_list, tag_list):
        """"""
        pass
