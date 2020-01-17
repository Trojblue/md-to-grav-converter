from handler import Handler
"""
TODO:
- 去掉所有 #
- remove [toc]
- 自定义footer

"""
class TextHandler (Handler):
    """
    处理文字相关, header, toc, 等等
    """
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)
