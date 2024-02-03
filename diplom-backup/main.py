import configparser
import requests
from pprint import pprint
import datetime
import json
from tqdm import tqdm

"""Функция преобразует дату загрузки фото в привычный формат"""
def time_convert(time_unix):
    time_bc = datetime.datetime.fromtimestamp(time_unix)
    str_time = time_bc.strftime('%Y-%m-%d time %H-%M-%S')
    return str_time

"""Функция возвращает ссылку на фото максимального размера и размер фото"""
def find_max_dpi(dict_in_search):
    max_dpi = 0
    need_elem = 0
    for j in range(len(dict_in_search)):
        file_dpi = dict_in_search[j].get('width') * dict_in_search[j].get('height')
        if file_dpi > max_dpi:
            max_dpi = file_dpi
            need_elem = j
    return dict_in_search[need_elem].get('url'), dict_in_search[need_elem].get('type')

class VK:
    """Метод для получения основных параметров в VK"""
    def __init__(self, access_token, user_id, version):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        self.json, self.export_dict = self._sort_info()

    """Метод для получения информации фотографий на стене в VK """    
    def get_profile_photos(self):
        params = {'owner.id': self.id, 'album_id': 'wall', 'extended': '1'}
        response = requests.get('https://api.vk.com/method/photos.get', params={**self.params, **params})
        photos_sizes_list = response.json()['response']
        return photos_sizes_list['count'], photos_sizes_list['items']

    """Метод для получения словаря с параметрами фотографий"""
    def get_logs_only(self):
        photo_count, photo_items = self.get_profile_photos()
        result = {}
        for i in range(photo_count):
           likes_count = photo_items[i]['likes']['count']
           url_download, picture_size = find_max_dpi(photo_items[i]['sizes'])
           time_warp = time_convert(photo_items[i]['date'])
           new_value = result.get(likes_count, [])
           new_value.append({'likes_count': likes_count,
                             'add_name': time_warp,
                             'url_picture': url_download,
                             'size': picture_size})
           result[likes_count] = new_value
        return result

    def _sort_info(self):
        """Метод для получения словаря с параметрами фотографий и списка JSON для выгрузки"""
        json_list = []
        sorted_dict = {}
        picture_dict = self.get_logs_only()
        for key, value in picture_dict.items():
            if len(value) == 1:
                file_name = f'{value[0]['likes_count']}.jpeg'
                json_list.append({'file name': file_name, 'size': value[0]['size']})
                sorted_dict[file_name] = picture_dict[key][0]['url_picture']
            else:
                for i in range(len(value)):
                    file_name = f'{value[i]["likes_count"]} {value[i]["add_name"]}.jpeg'
                    json_list.append({'file name': file_name, 'size': value[i-1]["size"]})
                    sorted_dict[file_name] = picture_dict[key][i]['url_picture']
        return json_list, sorted_dict

class Yandex:
    """Метод для получения основных параметров для загрузки фотографий на Ya.диск"""
    def __init__(self, folder_name, tokenYandex, num):
        self.token = tokenYandex
        self.added_files_num = num
        self.url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        self.headers = {'Authorization': self.token}
        self.folder = self._create_folder(folder_name)

    """Метод для создания папки на Ya.диске для загрузки фотографий"""    
    def _create_folder(self, folder_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}
        if requests.get(url, headers=self.headers, params=params).status_code != 200:
            requests.put(url, headers=self.headers, params=params)
            print(f'\nПапка {folder_name} успешно создана в корневом каталоге Яндекс диска\n')
        else:
            print(f'\nПапка {folder_name} уже существует. Файлы с одинаковыми именами не будут скопированы\n')
        return folder_name

    """Метод для получения ссылки для загрузки фотографий на Ya.диск"""
    def _in_folder(self, folder_name):    
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}
        resource = requests.get(url, headers=self.headers, params=params).json()['_embedded']['items']
        in_folder_list = []
        for elem in resource:
            in_folder_list.append(elem['name'])
        return in_folder_list

    """Метод загрузки фотографий на Ya.диск"""
    def create_copy(self, dict_files):
        files_in_folder = self._in_folder(self.folder)
        copy_counter = 0
        for key, i in zip(dict_files.keys(), tqdm(range(self.added_files_num))):
            if copy_counter < self.added_files_num:
                if key not in files_in_folder:
                    params = {'path': f'{self.folder}/{key}',
                              'url': dict_files[key],
                              'overwrite': 'false'}
                    requests.post(self.url, headers=self.headers, params=params)
                    copy_counter += 1
                else:
                    print(f'Внимание:Файл {key} уже существует')
            else:
                break

        print(f'\nЗапрос завершен, новых файлов скопировано (по умолчанию: 5): {copy_counter}'
              f'\nВсего файлов в исходном альбоме VK: {len(dict_files)}')

if __name__ == '__main__':
    access_token = 'substitute_VK_access_token'
    user_id = 'substitute_VK_id'
    version = '5.131'
    vk_client = VK(access_token, user_id, version)

    with open('my_VK_photo.json', 'w') as outfile:  # Сохранение JSON списка в файл my_VK_photo.json
        json.dump(vk_client.json, outfile)

    tokenYandex = 'substitute_Ya_token'
    def_photo_count = 5
    my_yandex = Yandex('VK_photo_backup', tokenYandex, def_photo_count)
    my_yandex.create_copy(vk_client.export_dict)  # Вызываем метод create_copy для копирования фотографий с VK на Ya.диск