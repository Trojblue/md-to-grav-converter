from handler import Handler
class TextHandler (Handler):
    """
    添加默认的yaml头文件
    """
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)
