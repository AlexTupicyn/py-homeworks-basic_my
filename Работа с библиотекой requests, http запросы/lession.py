import requests
import json

from pprint import pprint

# анкета на карту
# url_anketa = 'https://functions.yandexcloud.net/d4e8qsrmeednndemfsus'
# payload = {
#     "name": "тимур",
#     "surname": "тимур",
#     "patronymic": "тимур",
#     "telephone": "+7(111)111-11-11",
#     "birthdate": "1111-11-11",
#     "passport": "1111 11111111"
# }
# response = requests.post(url_anketa, json=payload)
# if 200 <= response.status_code < 300:
#     print(response.json())


url_yadisk = 'https://cloud-api.yandex.net'
headers_dict = {
    'Authorization': 'OAuth y0_AgAAAABnENF7AADLWwAAAADW0Zr0rLgkxmptRpqgS1mkh6kZ5279rAg'
}

# создание папки на ЯД
# url_create_folder = f'{url_yadisk}/v1/disk/resources'
# params_dict = {
#     'path': 'Image'
# }
#
# response = requests.put(url_create_folder,
#                         params=params_dict,
#                         headers=headers_dict)
# pprint(response)

# скачать файл
# url_image = 'https://imgtest.mir24.tv/uploaded/images/crops/2023/July/870x489_0x259_detail_crop_20230720121303_bb7da4e9_e4eb3f5ef3303ee23c6c7827fec55723597f0c7a88cfd13cf9bd380568ccfda7.jpg'
# response = requests.get(url_image)
# with open('капибара.jpg', 'wb') as file:
#     file.write(response.content)

# запросить url для загрузки
# url_get_upload = f'{url_yadisk}/v1/disk/resources/upload'
# response = requests.get(url_get_upload,
#                         headers=headers_dict,
#                         params={'path': 'Image/капибара.jpg'}
#                         )
# url_for_upload = response.json().get('href', '')
#
# # загрузить файл по этому пути
# with open('капибара.jpg', 'rb') as f:
#     response = requests.put(url_for_upload, files={"file": f})
#     print(response.status_code)

# params_dict = {
#     'api_key': 'DEMO_KEY',
#     'date': '2023-01-15'
# }
# response = requests.get('https://api.nasa.gov/planetary/apod', params=params_dict)
#
# response = requests.get(response.json().get('url'))
# with open('image.jpg', 'wb') as file:
#     file.write(response.content)


my_heroes = ['Spider-Man', 'Black Widow', 'Wyatt Wingfoot']
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
heroes_info = requests.get(url).json()
for hero_info in heroes_info:
    hero_name = hero_info.get('name')
    if hero_name in my_heroes:
        print(hero_name, hero_info.get('powerstats', {}).get('durability'))


# heroes = [
#     {
#         'name': '123124',
#         'powerstats': {
#             "intelligence": 38,
#             "strength": 100,
#             "speed": 17,
#             "durability": 80,
#             "power": 24,
#             "combat": 64
#         }
#     },
#     {
#         'name': 'dfhdfh'
#     },
# ]
# for hero_info in heroes:
#     hero_name = hero_info.get('name')
#     print(hero_name, hero_info.get('powerstats', {}).get('durability', 'занчение по умолчанию'))
