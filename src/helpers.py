import json
import re


class ParserHelper:
    @staticmethod
    def list_to_num(l: list) -> int:
        if len(l) <= 0:
            raise IndexError("Empty list")
        numbers = [x for x in re.findall(r'-?\d+\.?\d*',''.join(l))]
        if not numbers:
            raise ValueError("No numbers")
        return int(float(numbers[0]))

    @staticmethod
    def format_rating(l: list) -> float:
        if len(l) <= 0:
            return 0
        return float(''.join(x.text for x in l).replace(',', '.'))

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
