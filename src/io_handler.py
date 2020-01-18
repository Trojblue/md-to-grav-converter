import fileinput
import os
from converter import Converter
from handler import Handler

"""
File operation handler;
- write
- read
"""


class IOHandler(Handler):
    """
    添加默认的yaml头文件
    """

    def __init__(self, converter: Converter):
        super().__init__(converter)
        c = self.converter
        self.out_folder_path = os.path.join(c.output_path, c.folder_name)
        self.out_md_path = os.path.join(self.out_folder_path, "%s.md" % (c.page_type))
        self.init_folder()

    def init_folder(self):
        """初始化输出目录, 创建空输出文件夹和空md文件
        """
        output_path = self.converter.output_path
        if not os.path.exists(output_path):  # create output dir
            os.mkdir(output_path)
        if not os.path.exists(self.out_folder_path):  # create folder dir
            os.mkdir(self.out_folder_path)

        open(self.out_md_path, 'a').close()  # create empty md file

    def write_yaml(self):
        """把temp.yaml写入Grav Folder里的*.md
        """
        c = self.converter
        out_md_path = os.path.join(c.output_path, c.folder_name, "%s.md" % (c.page_type))

        print("writing yaml to %s ..." % out_md_path)

        with open(out_md_path, 'r+', encoding="utf-8") as md, \
                fileinput.input(self.converter.yaml_path, openhook=fileinput.hook_encoded("utf-8")) as yaml:
            md_content = md.read()
            md.seek(0)
            md.write("---\n")
            try:
                for line in yaml:  # todo: 当前写法如果没找到 *.yaml, 会在md文件里留下两行"---"
                    md.write(line)
            except FileNotFoundError:
                print("===ERROR===\n Temporary YAML File Not Found, consider generating it first")
            md.write("\n---\n")
            md.write(md_content)
