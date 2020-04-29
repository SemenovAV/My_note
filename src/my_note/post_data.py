from typing import Optional

import requests

from src.my_note.get_time_name import ge_time_name


def post_data(data: bytes, token: str, ) -> Optional[bool]:
    """
    Функция сохраняет переданны данные на яндекс диск.

    :param data: Данные для сохранения
    :param token: str OAuth-токен яндекс диска.
    :return: В случае ошибки сети вернет False. В остальных случаях вернет ответ сервера.
    """
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    filename = ge_time_name()

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
            requests.put(json_['href'], data=data)
            return json_
    except requests.exceptions.BaseHTTPError as e:
        print(e)
        return False
