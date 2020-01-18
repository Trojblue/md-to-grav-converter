from converter import Converter
from handler import Handler
from datetime import datetime
from typing import Dict
import yaml

"""

"""

class YAMLHandler (Handler):
    """
    添加默认的yaml头文件
    """

    def __init__(self, converter: Converter):
        super().__init__(converter)  # todo: maybe wrong here
        self._yaml_dict = {}

    def set_title(self, title: str) -> None:
        self._yaml_dict["title"] = title
        return

    def set_summary(self, summary: bool) -> None:
        if summary:
            self._yaml_dict['summary'] = {'enabled': '1'}
        else:
            self._yaml_dict['summary'] = {'enabled': '0'}
        return

    def set_media_order(self):
        """默认按时间顺序
        """
        pass

    def set_date(self, time: datetime) -> None:
        """添加时间戳
        """
        self._yaml_dict['date'] = time.strftime('%H:%M %d-%m-%Y')
        return

    def set_taxonomy(self, category_list, tag_list) -> None:
        """"""
        self._yaml_dict["taxonomy"] = {
            'category': category_list,
            'tag': tag_list}
        return

    def get_yaml_dict(self) -> Dict:
        return self._yaml_dict

    def dump_yaml(self):
        """把dictionary内容写入到temp.yaml
        """
        c = self.converter
        with open(c.yaml_path, 'w') as f:
            data = yaml.dump(self._yaml_dict, f, allow_unicode=True)
        print("temporary yaml file created at %s" % c.yaml_path)
