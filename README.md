# Парсер отзывов c Yandex Карт

Скрипт парсит отзывы с Yandex Карт<br>
Для парсинга необходимо указать id компании в начале обработки скрипта

По результатам выполнения, возвращается объект, в котором:
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
      "stars": 5
    },
    {
      "name": "Иван Иванов",
      "icon_href": "https://avatars.mds.yandex.net/get-yapic/51381/cs8Tx0sigtfayYhRQBDJkavzJU-1/islands-68",
      "date": 1681992580.04,
      "text": "Выражаю огромную благодарность работникам ",
      "stars": 5
    }
  ]
}
```


Необходимо установить библиотеку<br>
```shell
pip install yandex-reviews-parser
```

```python
id_ya = 1234 #ID Компании Yandex
parser = YandexParser(id_ya)

all_data = parser.parse() #Получаем все данные
company = parser.parse(type_parse='company') #Получаем данные по компании
reviews = parser.parse(type_parse='company') #Получаем список отзывов
```