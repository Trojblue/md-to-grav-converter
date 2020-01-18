import fileinput, os, re
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
        """把临时yaml写入Grav Folder里的*.md
        yaml文件的位置由converter确定
        todo: 当前写法如果没找到 *.yaml, 会在md文件里留下两行"---"; 目标: 如果已经存在两行"---", 删除旧yaml再添加新的
        """
        c = self.converter
        out_md_path = os.path.join(c.output_path, c.folder_name, "%s.md" % (c.page_type))
        remove_old_yaml(out_md_path)

        print("writing yaml to %s ..." % out_md_path)

        with open(out_md_path, 'r+', encoding="utf-8") as md, \
                fileinput.input(c.yaml_path, openhook=fileinput.hook_encoded("utf-8")) as yaml:
            try:  # 测试tmp.yaml是否存在
                tmp = yaml[0]
            except FileNotFoundError:
                print("===ERROR===\n Temporary YAML File Not Found, consider generating it first")

            md_content = md.read()
            md.seek(0)
            # 写入yaml
            md.write("---\n")
            for line in yaml:
                md.write(line)
            md.write("\n---\n")
            # 写入原有markdown内容
            md.write(md_content)
        print("write complete")

    def write_md(self):
        pass


def remove_old_yaml(file: str) -> bool:
    """检测文件是否有yaml header (用 --- 分隔), 如果存在的话就删除;
    return: 是否曾经有旧yaml
    """
    has_yaml = False
    f = open(file, 'r+', encoding="utf-8")
    lines = f.readlines()
    f.seek(0)

    yaml_pattern = '---\s*$'

    if re.match(yaml_pattern, lines[0]):  # has old yaml, remove it;
        print("removing old yaml header...")
        has_yaml = True
        yaml_ends = False
        for line in lines[1:]:  # delete lines between first two "---" marks
            if (yaml_ends):
                f.write(line)
            elif re.match(yaml_pattern, line):
                yaml_ends = True
        f.truncate()

    f.close()
    return has_yaml
