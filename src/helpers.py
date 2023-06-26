import json
import re


class ParserHelper:
    @staticmethod
    def list_to_num(l:list)->int:
        return int([x for x in re.findall(r'-?\d+\.?\d*', l)][0])

    @staticmethod
    def format_rating(data:list)-> float:
        return float(''.join(x.text for x in data).replace(',', '.'))

    @staticmethod
    def write_json_txt(result, file):
        """
        Записать новый файл JSON
        :param result:
        :param file:
        :return:
        """
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)