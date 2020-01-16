from handler import Handler
class TextHandler (Handler):
    """
    处理文字相关, header, toc, 等等
    """
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)
