import requests
import datetime
from typing import Optional


def post_note(filename: str, token: str, data: str = '') -> Optional[dict]:
    """
    Функция сохраняет переданный файл или текстовые данные на яндекс диск
    :param filename: str Имя файла
    :param token: str OAuth-токен яндекс диска.
    :param data: str Текст
    :return:
    """
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    if data:
        data = data.encode('utf-8')
        time = datetime.datetime.now().strftime('%H-%M-%S')
        path = datetime.datetime.now().strftime('%d.%m.%Y')

        filename = f'/{path}/{time}{filename}'
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
