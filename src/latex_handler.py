from handler import Handler
class LatexHandler (Handler):
    """
    处理图像相关
    """
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)

    def handle_latex(self, og: str) -> str:
        """
        输入不含$号的latex, 输出整理后的latex; 比如:\R变成 \mathbb{R}
        :param og:
        :return:
        """
        pass
