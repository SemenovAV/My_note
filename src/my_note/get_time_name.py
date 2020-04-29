import datetime


def ge_time_name(postfix: str = 'note', ext: str = 'txt', time: bool = True, date: bool = True) -> str:
    """

    :param postfix: Желаемый постфикс.
    :param ext: Желаемое расширение.
    :param time: Включать ли время в название.
    :param date: Включать ли дату в название.
    :return:
    """
    t = datetime.datetime.now().strftime('%H-%M-%S')
    d = datetime.datetime.now().strftime('%d.%m.%Y')
    return f'/{d if date else ""}_{t if time else ""}_{postfix}.{ext}'
