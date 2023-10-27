# Парсер отзывов c Yandex Карт

Скрипт парсит отзывы с Yandex Карт<br>
Для парсинга необходимо указать id компании в начале обработки скрипта

По результатам выполнения, возвращается объект.

---
Необходимо установить библиотеку<br>
```shell
pip install yandex-reviews-parser
```
---
Примеры использования
```python
from yandex_reviews_parser.utils import YandexParser
id_ya = 1234 #ID Компании Yandex
parser = YandexParser(id_ya)

all_data = parser.parse() #Получаем все данные
```
```json
{
  "company_info": {
    "name": "Дилерский центр Hyundai",
    "rating": 5.0,
    "count_rating": 380,
    "stars": 5
  },
  "company_reviews": [
    {
      "name": "Иван Иванов",
      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",
      "date": 1681992580.04,
      "text": "Выражаю огромную благодарность работникам ",
      "stars": 5,
      "answer": "Владимир, Благодарим Вас, что уделили время и оставили приятный отзыв о нашем автосервисе! Мы для Вас приготовили подарок в следующий визит."
    },
    {
      "name": "Иван Иванов",
      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",
      "date": 1681992580.04,
      "text": "Выражаю огромную благодарность работникам ",
      "stars": 5,
      "answer": null
    }
  ]
}
```
---
```python
from yandex_reviews_parser.utils import YandexParser
id_ya = 1234 #ID Компании Yandex
parser = YandexParser(id_ya)

company = parser.parse(type_parse='company') #Получаем данные по компании
```
```json
{
  "company_info": {
    "name": "Дилерский центр Hyundai",
    "rating": 5.0,
    "count_rating": 380,
    "stars": 5
  }
}
```
---
```python
from yandex_reviews_parser.utils import YandexParser
id_ya = 1234 #ID Компании Yandex
parser = YandexParser(id_ya)

reviews = parser.parse(type_parse='company') #Получаем список отзывов
```
```json
{
  "company_reviews": [
    {
      "name": "Иван Иванов",
      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",
      "date": 1681992580.04,
      "text": "Выражаю огромную благодарность работникам ",
      "stars": 5,
      "answer": "Владимир, Благодарим Вас, что уделили время и оставили приятный отзыв о нашем автосервисе! Мы для Вас приготовили подарок в следующий визит."
    },
    {
      "name": "Иван Иванов",
      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",
      "date": 1681992580.04,
      "text": "Выражаю огромную благодарность работникам ",
      "stars": 5,
      "answer": null
    }
  ]
}
```

---
Для работы скрипта у Вас должен быть установлен ChromeDriver. <br>
Для запуска скрипта в докере, прикладываю свой Dockerfile.

```Dockerfile
FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y gettext
RUN apt-get install -y wget xvfb unzip

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

RUN pip install --upgrade pip

COPY req.txt .

RUN pip install -r req.txt

COPY . .

RUN python main.py
```