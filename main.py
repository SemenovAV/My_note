import json

from src.my_note.app import app
"""
Для запуска нужно указать OAuth-токен яндекс диска в app.config.json
"""

if __name__ == '__main__':
    with open('src/app.config.json', encoding='utf8') as f:
        config = json.load(f)
    token = config.get('token')
    if token:
        print(app(token))
