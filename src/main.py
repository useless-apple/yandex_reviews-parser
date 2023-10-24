from helpers import ParserHelper
from utils import YandexParser

if __name__ == '__main__':
    id_ya = 1793912303
    parser = YandexParser(int(id_ya))
    ParserHelper.write_json_txt(parser.parse(), 'result_all.json')

