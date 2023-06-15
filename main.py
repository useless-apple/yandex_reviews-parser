import undetected_chromedriver
import time

from helpers import ParserHelper
from parsers import Parser

if __name__ == '__main__':
    id_ya = input('Введите id компании Яндекс')
    url = 'https://yandex.ru/maps/org/{}/reviews/'.format(str(id_ya))
    opts = undetected_chromedriver.ChromeOptions()
    opts.add_argument('headless')
    opts.add_argument('--disable-gpu')
    driver = undetected_chromedriver.Chrome(options=opts)
    parser = Parser(driver)
    driver.get(url)
    time.sleep(4)
    try:
        parser.parsing()
    except Exception as e:
        print(e)
    finally:
        parser.driver.close()
        parser.driver.quit()
        print(parser.result)
        ParserHelper.write_json_txt(parser.result, 'result.json')
