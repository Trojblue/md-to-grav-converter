import os
import converter, io_handler, yaml_handler
import yaml
import re
import fileinput
from typing import *
from datetime import datetime

SAMPLE_MD = os.path.join(os.path.dirname(os.getcwd()), "bin", "sample_item.zh.md")
SAMPLE_YAML = os.path.join(os.path.dirname(os.getcwd()), "bin", "sample.yaml")

TEST_YAML = os.path.join(os.path.dirname(os.getcwd()), "bin", "test_output.yaml")
TEST_MD = os.path.join(os.path.dirname(os.getcwd()), "bin", "test.md")


# 返回sample dictionary
def get_yaml_sample() -> Dict:
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


def try_converter():
    """
    输入: bin/test.md, src/temp.yaml
    输出: /outputs/test_md_folder/sample_item.zh.md
    """
    c = converter.Converter(TEST_MD, "test_md_folder")
    print(c)
    io = io_handler.IOHandler(c)
    # print(c)
    io.write_yaml()


def try_re():
    pattern = '---\s*$'
    test_string = '---\n'
    result = re.match(pattern, test_string)

    if result:
        print("Search successful.")
    else:
        print("Search unsuccessful.")


def try_datetime():
    # datestr = "03:24 2020-03-17"
    # datetime_object = datetime.strptime(datestr, '%H:%M %Y-%m-%d')
    # print(datetime_object)
    time = datetime.today()
    a = time.strftime('%H:%M %d-%m-%Y')
    print("type: %s \n content: %s" % (type(a), a))


def try_dump():
    c = converter.Converter(TEST_MD, "test_md_folder")
    yh = yaml_handler.YAMLHandler(c)
    yh.set_title("测试标题")
    yh.set_date(datetime.today())
    yh.set_summary(True)
    yh.set_taxonomy(['学习'], ['tag1', 'tag2', '中文tag'])

    yaml_dict = yh.get_yaml_dict()
    print(yaml_dict, "<- yaml dict")
    yh.dump_yaml()


if __name__ == '__main__':
    try_dump()
