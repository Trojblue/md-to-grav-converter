import os
import converter, io_handler, yaml_handler
import yaml
import fileinput
from typing import *

SAMPLE_MD = os.path.join(os.path.dirname(os.getcwd()), "bin", "test.md")
SAMPLE_YAML = os.path.join(os.path.dirname(os.getcwd()), "bin", "sample.yaml")

TEST_YAML = os.path.join(os.path.dirname(os.getcwd()), "bin", "test.yaml")


def try_read():
    with open("test.md", 'r') as t:
        lines = t.readlines()
        print(t, lines)
    pass
def try_read2():
    with open("test.md", "r") as t:
        lines = t.readlines()
def try_parent_dir():
    # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(os.path.abspath(os.path.dirname(os.getcwd())))
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))
    print(  os.path.join(os.path.dirname(os.getcwd()), "bin", "test.md")    )


def try_mkdir():
    os.mkdir('D:\\CSC\\Github\\md-to-grav-converter\\outputs')


def try_converter():
    c = converter.Converter(SAMPLE_MD, "sample_md_folder")
    io = io_handler.IOHandler(c)
    # print(c)
    io.write_yaml()


# 返回sample dictionary
def yaml_sample() -> Dict:
    # with open(SAMPLE_YAML, 'r', encoding="utf-8") as yaml_file:
    #     yaml_dict = yaml.load(yaml_file)

    sample_yaml_dict = {'title': '解决Grav CMS迁移后的404问题',
                        'date': '03:45 29-12-2019',
                        'taxonomy': {
                            'category': ['blog'],
                            'tag': ['Grav', 'Linux', '前端', 'VPS']},
                        'summary': {
                            'enabled': '1'},
                        'feed': {'limit': 10},
                        'aura': {
                            'pagetype': 'website'}
                        }
    return sample_yaml_dict


def try_yaml():
    with open(TEST_YAML, 'w') as f:
        data = yaml.dump(yaml_sample(), f)


def try_concat():
    with open(SAMPLE_MD, 'r+', encoding="utf-8") as md, \
            fileinput.input(SAMPLE_YAML, openhook=fileinput.hook_encoded("utf-8")) as fin:
        md_content = md.read()
        md.seek(0)
        md.write("---\n")
        for line in fin:
            md.write(line)
        md.write("\n---\n")
        md.write(md_content)



if __name__ == '__main__':
    try_converter()

