from handler import Handler
"""
TODO:
- title
- media_order
- date
- taxonomy
- summary

"""
class TextHandler (Handler):
    """
    添加默认的yaml头文件
    """
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)

    def set_title(self, title):
        pass

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
