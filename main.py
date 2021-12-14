import json

import cfscrape
import requests
from bs4 import BeautifulSoup

yandex_id = '167689226141'


def get_count_star(review_stars):
    star_count = 0
    for review_star in review_stars:
        if '_empty' in review_star.get('class'):
            continue
        elif '_half' in review_star.get('class'):
            star_count = star_count + 0.5
        else:
            star_count = star_count + 1
    return star_count


def get_session():
    session = requests.Session()
    session.headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'viewport-width': '1920'
    }
    return cfscrape.create_scraper(sess=session)


def parsing_data(data_result, r):
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        reviews = soup.find('div', {"data-chunk": "reviews"})
    except:
        return None
    try:
        summary_rating__main = reviews.find('div', {"class": "business-summary-rating__main-rating"})
    except:
        summary_rating__main = None
    try:
        rank_summary_rating__main = summary_rating__main.find('span',
                                                              {
                                                                  "class": "business-summary-rating-badge-view__rating"}).text
    except:
        rank_summary_rating__main = None
    try:
        count_summary_rating__main = summary_rating__main.find('div', {
            "class": "business-summary-rating-badge-view__rating-count"}).text
    except:
        count_summary_rating__main = None
    try:
        stars_summary_rating__main = get_count_star(
            summary_rating__main.find('div', {"class": "business-rating-badge-view__stars"}))
    except:
        stars_summary_rating__main = None
    data_result['company_info'] = {
        'company_rating': rank_summary_rating__main,
        'company_count_reviews': count_summary_rating__main,
        'company_count_stars': stars_summary_rating__main
    }
    try:
        reviews_list = reviews.find('div', {"class": "business-reviews-card-view__reviews-container"})
    except:
        reviews_list = None
    if reviews_list:
        review_id = 0
        for review in reviews_list:
            try:
                review_name = review.find('div', {"itemprop": "author"}).find('span', {"itemprop": "name"}).text
            except:
                review_name = None
            try:
                review_date = review.find('meta', {"itemprop": "datePublished"}).get('content')
            except:
                review_date = None
            try:
                review_text = review.find('span', {"class": "business-review-view__body-text"}).text
            except:
                review_text = None
            try:
                star_count = get_count_star(review.find('div', {"class": "business-rating-badge-view__stars"}))
            except:
                star_count = None
            data_result['company_reviews'].append({
                'review_name': review_name,
                'review_date': review_date,
                'review_text': review_text,
                'star_count': star_count
            })
            review_id = review_id + 1
    return data_result


url = 'https://yandex.ru/maps/org/' + yandex_id + '/reviews/'
session = get_session()
r = session.get(url)
data_result = {
    'company_info': {},
    'company_reviews': []
}
data_result = parsing_data(data_result, r)
if len(data_result['company_reviews']) == 0 or len(data_result['company_info']) == 0:
    data_result = None
with open('company_reviews.json', 'w', encoding='utf-8') as f:
    json.dump(data_result, f, ensure_ascii=False, indent=4)
print('Parsing Success')
