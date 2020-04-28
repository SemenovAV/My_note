import requests
from typing import Optional
import datetime


def create_puth(token: str) -> Optional[dict]:
    """
    Функция создает новую папку на яндекс диске

    :param name: Имя папки
    :param token: str OAuth-токен яндекс диска.
    :return: bool результат операции
    """
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    path = datetime.datetime.now().strftime('%d.%m.%Y')

    headers = {
        'Authorization': f'OAuth {token}'
    }
    params = {
        'path': path,
    }
    try:
        response = requests.put(url, headers=headers, params=params)
        json_ = response.json()
        return json_
    except requests.exceptions.BaseHTTPError:
        return