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
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)
        self._yamlList = []
        self.title = ""

    def set_title(self):
        self.title = input("input the title:")
        self._yamlList.append("title: \'%s\'"%(self.title))

    def set_summary(self):
        summary = input("input the summary: leave [blank] to use title; type [N] to not use summary")
        if summary == "":
            summary = self.title
        elif summary == "N" or summary == "n":
            self._yamlList.append(["Summary:",
                                   ["    enabled: \'0\'"] ])
            return
        self._yamlList.append(["Summary:",
                               ["    enabled: \'1\'"] ])
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

    def set_summary(self):
        """set default summary for item
        """
        pass
