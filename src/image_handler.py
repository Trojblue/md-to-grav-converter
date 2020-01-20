from handler import Handler
from converter import Converter
"""

## Pending Features
- 检测重复图片
- 上传到图床, 留下本地备用链接
- resize
- 绝对路径图片转相对路径

## Notes
自动上传: https://github.com/chchuj/useful_script/blob/master/Scripts/md%E6%96%87%E4%BB%B6%E5%9B%BE%E7%89%87%E5%9B%BE%E5%BA%8A%E8%BD%AC%E6%8D%A2/md_transfer_v3
删除没用过的图: https://github.com/chchuj/useful_script/blob/master/Scripts/%E6%9F%A5%E6%89%BE%E9%A1%B9%E7%9B%AE%E4%B8%AD%E5%BA%9F%E5%BC%83%E7%9A%84%E5%9B%BE%E7%89%87/unuse_img.py

"""
class ImageHandler(Handler):

    def __init__(self, converter: Converter):
        super().__init__(converter)

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
