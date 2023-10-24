import json
import re
from datetime import datetime
from typing import Union


class ParserHelper:
    @staticmethod
    def list_to_num(l: list) -> int:
        """
        Преобразует пришедший массив в первое попавшееся число
        @param l: ['321fdfd','fdfd']
        @return: Число 321
        """
        if len(l) <= 0:
            raise IndexError("Empty list")
        numbers: list = [x for x in re.findall(r'-?\d+\.?\d*', ''.join(l))]
        if not numbers:
            raise ValueError("No numbers")
        return int(float(numbers[0]))

    @staticmethod
    def format_rating(l: list) -> float:
        """
        Форматирует рейтинг в число с плавающей точкой
        @param l: Массив значений ['1','.','5']
        @return: Число с плавающей точкой 1.5
        """
        if len(l) <= 0:
            return 0
        return float(''.join(x.text for x in l).replace(',', '.'))

    @staticmethod
    def write_json_txt(result, file) -> None:
        """
        Записать новый файл JSON
        :param result: JSON Объект который нужно записать
        :param file: Название файла (вместе с .json)
        :return: None
        """
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

    @staticmethod
    def form_date(date_string: str) -> float:
        """
        Приводим дату в формат Timestamp
        :param date_string: Дата в формате %Y-%m-%dT%H:%M:%S.%fZ
        :return: Дата в формате Timestamp
        """
        datetime_object: datetime = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        return datetime_object.timestamp()

    @staticmethod
    def get_count_star(review_stars: list) -> Union[float, int]:
        """
        Считаем рейтинг по звездам
        :param review_stars: Массив элементов звезд рейтинга
        :return: Рейтинг
        """
        star_count: float = 0
        for review_star in review_stars:
            if '_empty' in review_star.get_attribute('class'):
                continue
            if '_half' in review_star.get_attribute('class'):
                star_count = star_count + 0.5
                continue
            star_count = star_count + 1
        return star_count
