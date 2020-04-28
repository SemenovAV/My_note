import requests
import datetime
from typing import Optional
from src.tools.create_path import create_puth


def post_file(file_path: str, token: str,) -> Optional[dict]:
    """
    Функция сохраняет переданный файл или текстовые данные на яндекс диск
    :param file_path: str Имя файла.
    :param token: str OAuth-токен яндекс диска.
    :return:
    """
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    time = datetime.datetime.now().strftime('%H-%M-%S')
    path = datetime.datetime.now().strftime('%d.%m.%Y')

    if file_path:
        with open(file_path, 'rb') as f:
            data = f.read()
        filename = f'/{path}/{time}{file_path}'
        headers = {
            'Authorization': f'OAuth {token}'
        }
        params = {
            'path': filename,
            'overwrite': False
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            json_ = response.json()
            if json_.get('href'):
                 r = requests.put(json_['href'], data=data)
                 return r
            else:
                return json_
        except requests.exceptions.BaseHTTPError as e:
            return
