from handler import Handler
class ImageHandler(Handler):
    """
    处理图像相关
    """
    def __init__(self, file_path, output_path):
        super().__init__(file_path, output_path)

    def handle_resize(self, og:str) ->str:
        """
        输入Typora图像代码, 输出对应的Grav版本
        - 百分比缩放变成写死的分辨率

        :param og: Original Image Code
        :return: Image Code for grav
        """
        pass

    def handle_upload(self, og:str) -> bool:
        """
        添加alt-link, 上传到图床;
        :param og:
        :return:
        """

def change_img(old_file:str, new_file:str):
    """

    :param old_file:
    :param new_file:
    :return:
    """
    old_file = open(old_file, "W+")
    lines = old_file.readlines()
    old_file.close()
    for line in lines:
        rs = line.rstrip('\n')
        new_file = open(new_file, 'a')
        new_file.write("Something")
        new_file.close()
