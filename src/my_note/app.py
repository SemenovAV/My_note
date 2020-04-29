import sys
from typing import Optional

from src.my_note.post_data import post_data


def app(token: str) -> Optional[bool]:
    """
    Принемает в качестве параметров запуска:
      текст и опционально (после --file ) путь к файлу
        для загрузки - сохраняет на яндекс диск (нужен OAuth-токен яндекс диска)
        Возможно передавать одновременно и текст и файл, но тогда сначало
        текст а потом путь к файлу:
        app.py привет мир --file main_file
    :param token:
    :return:
    """
    option = [i for i, x in enumerate(sys.argv[1:]) if x == '--file'] or len(sys.argv)
    option = option[0]
    text = ' '.join(sys.argv[:option:])
    path = sys.argv[option + 2:]
    result = []
    if len(path) > 0:
        try:
            with open(path[0], 'rb') as f:
                data = f.read()
            result.append(post_data(data, token))

        except Exception as e:
            result.append(e)
    if text:
        try:
            text = text.encode('utf-8')
            result.append(post_data(text, token))
        except Exception as e:
            print(e)

    else:
        print('No data!')
        return False
