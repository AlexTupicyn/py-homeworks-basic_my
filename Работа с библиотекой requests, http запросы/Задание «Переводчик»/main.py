import requests

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20220928T183617Z.4449b33063fe4328.b93679d48620ed6f3c20da6bff0237bcbd0e8d6a'  # токен из подсказки


def translate_word(word: str) -> str:
    param = {'key': token,
             'lang': 'ru-en',
             'text': word,
             'ui': 'ru'
             }
    response = requests.get(url=url, params=param).json()
    trans_word = response['def'][0]['tr'][0]['text']
    print(trans_word)
    return trans_word


if __name__ == '__main__':
    word = 'машина'
    assert translate_word(word) == 'car'
