import time
from dataclasses import asdict
from datetime import datetime
from typing import Union

from selenium.webdriver.common.by import By

from helpers import ParserHelper
from storage import Review, Info


class Parser:
    def __init__(self, driver):
        self.result = {
            'company_info': {},
            'company_reviews': []
        }
        self.driver = driver

    @staticmethod
    def form_date(date_string: str) -> float:
        """
        Приводим дату в формат Timestamp
        :param date_string: Дата в формате %Y-%m-%dT%H:%M:%S.%fZ
        :return: Дата в формате Timestamp
        """
        datetime_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        return datetime_object.timestamp()

    @staticmethod
    def get_count_star(review_stars: list) -> Union[float, int]:
        """
        Считаем рейтинг по звездам
        :param review_stars: Массив элементов звезд рейтинга
        :return: Рейтинг
        """
        star_count = 0
        for review_star in review_stars:
            if '_empty' in review_star.get_attribute('class'):
                continue
            if '_half' in review_star.get_attribute('class'):
                star_count = star_count + 0.5
                continue
            star_count = star_count + 1
        return star_count

    def __scroll_to_bottom(self, elem, driver) -> None:
        """
        Скроллим список до последнего отзыва
        :param elem: Последний отзыв в списке
        :param driver: Драйвер undetected_chromedriver
        :return: None
        """
        driver.execute_script(
            "arguments[0].scrollIntoView();",
            elem
        )
        time.sleep(1)
        new_elem = driver.find_elements(By.CLASS_NAME, "business-reviews-card-view__review")[-1]
        if elem == new_elem:
            return
        self.__scroll_to_bottom(new_elem, driver)

    def __get_data_item(self, elem):
        """
        Спарсить данные по отзыву
        :param elem: Отзыв из списка
        :return: Словарь
        {
            name: str
            icon_href: Union[str, None]
            date: float
            text: str
            stars: float
        }
        """
        name = elem.find_element(By.XPATH, ".//span[@itemprop='name']").text
        try:
            icon_href = elem.find_element(By.XPATH, ".//div[@class='user-icon-view__icon']").get_attribute('style')
            icon_href = icon_href.split('"')[1]
        except:
            icon_href = None

        date = elem.find_element(By.XPATH, ".//meta[@itemprop='datePublished']").get_attribute('content')

        text = elem.find_element(By.XPATH, ".//span[@class='business-review-view__body-text']").text

        stars = elem.find_elements(By.XPATH, ".//div[@class='business-rating-badge-view__stars']/span")
        stars = self.get_count_star(stars)

        item = Review(
            name=name,
            icon_href=icon_href,
            date=self.form_date(date),
            text=text,
            stars=stars
        )
        return asdict(item)

    def __get_data_campaign(self) -> dict:
        """
        Получаем данные по компании.
        :return: Словарь данных
        {
            name: str
            rating: float
            count_rating: int
            stars: float
        }
        """
        xpath_name = ".//h1[@class='orgpage-header-view__header']"
        name = self.driver.find_element(By.XPATH, xpath_name).text

        xpath_rating_block = ".//div[@class='business-summary-rating-badge-view__rating-and-stars']"
        rating_block = self.driver.find_element(By.XPATH, xpath_rating_block)

        xpath_rating = ".//div[@class='business-summary-rating-badge-view__rating']/span[contains(@class, 'business-summary-rating-badge-view__rating-text')]"
        rating = rating_block.find_elements(By.XPATH, xpath_rating)
        rating = ParserHelper.format_rating(rating)

        xpath_count_rating = ".//div[@class='business-summary-rating-badge-view__rating-count']/span[@class='business-rating-amount-view _summary']"
        count_rating_list = rating_block.find_element(By.XPATH, xpath_count_rating).text
        count_rating = ParserHelper.list_to_num(count_rating_list)

        xpath_stars = ".//div[@class='business-rating-badge-view__stars']/span"
        stars = self.get_count_star(rating_block.find_elements(By.XPATH, xpath_stars))
        item = Info(
            name=name,
            rating=rating,
            count_rating=count_rating,
            stars=stars
        )
        return asdict(item)

    def parsing(self):
        """
        Начинаем парсить данные
        :return: None
        """
        self.result['company_info'] = self.__get_data_campaign()
        elements = self.driver.find_elements(By.CLASS_NAME, "business-reviews-card-view__review")
        self.__scroll_to_bottom(elements[-1], self.driver)
        elements = self.driver.find_elements(By.CLASS_NAME, "business-reviews-card-view__review")
        for elem in elements:
            self.result['company_reviews'].append(self.__get_data_item(elem))