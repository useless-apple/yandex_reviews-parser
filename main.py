from helpers import ParserHelper
from utils import YandexParser

if __name__ == '__main__':
    id_ya = input("Введите ID яндекс компании: ")
    parser = YandexParser(int(id_ya))
    ParserHelper.write_json_txt(parser.parse(), 'result_all.json')

