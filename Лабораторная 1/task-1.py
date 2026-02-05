from typing import Union
import doctest
# TODO Написать 3 класса с документацией и аннотацией типов

class TV:
    def __init__(self, volume: int, channel_number: int):
        """
        Создание и подготовка к работе объекта "Телевизор"

        :param volume: Громкость телевизора от 0 до 100
        :param channel_number: Номер канала на телевизоре

        Примеры:
        >>> tv = TV(50, 52)  # инициализация экземпляра класса
        """
        if not isinstance(volume, int):
            raise TypeError("Громкость телевизора должна быть типа int")
        if volume < 0 or volume > 100:
            raise ValueError("Громкость телевизора должна быть числом от 0 до 100")
        self.volume = volume


        if not isinstance(channel_number, int):
            raise TypeError("Номер канала на телевизоре должен быть типа int")
        if not channel_number > 0:
            raise ValueError("Номер канала на телевизоре должен быть положительным числом")
        self.channel_number = channel_number

    def change_volume(self, change_v: int) -> None:
        """
        Изменение громкости телевизора.
        :param change_v: Изменение громкости телевизора

        :raise ValueError: Если новая громкость телевизора не является числом от 0 до 100

        Примеры:
        >>> tv = TV(40, 67)
        >>> tv.change_volume(-20)
        """
        if not isinstance(change_v, int):
            raise TypeError("Изменение громкости телевизора должно быть типа int")
        if self.volume + change_v < 0 or self.volume + change_v > 100:
            raise ValueError("Новая громкость телевизора должна быть числом от 0 до 100")
        ...
    def change_channel(self, new_channel_number: int) -> None:
        """
        Изменение канала на телевизоре.
        :param new_channel_number: Новый номер канала на телевизоре

        :raise ValueError: Если новый номер канала на телевизоре не является положительным числом
        Примеры:
        >>> tv = TV(15, 42)
        >>> tv.change_channel(5)
        """
        if not isinstance(new_channel_number, int):
            raise TypeError("Новый номер канала должен быть типа int")
        if not new_channel_number > 0:
            raise ValueError("Новый номер канала на телевизоре должен быть положительным числом")
        ...

class Phone:
    def __init__(self, battery_level: int, storage_used: Union[int, float], is_on: bool):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param battery_level: Уровень заряда батареи от 0 до 100
        :param storage_used: Использованная память в Гб, до 512 Гб
        :param is_on: Включен ли телефон
        Примеры:
        >>> phone = Phone(69, 37, True)  # инициализация экземпляра класса
        """
        if not isinstance(battery_level, int):
            raise TypeError("Уровень заряда батареи должен быть типа int")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда батареи должен быть числом от 0 до 100")
        self.battery_level = battery_level


        if not isinstance(storage_used, (int, float)):
            raise TypeError("Использованная память должна быть типа int или float")
        if storage_used < 0 or storage_used > 512:
            raise ValueError("Использованная память должна быть числом от 0 до 512 Гб")
        self.storage_used = storage_used

        if not isinstance(is_on, bool):
            raise TypeError("Включен ли телефон должно быть тип bool")
        self.is_on = is_on

    def charge(self, percentage: int) -> None:
        """
        Зарядка батареи на даноое количество процентов
        :param percentage: Изменение заряда батареи

        :raise ValueError: Если новый уровень заряда батареи не является числом от 0 до 100

        :raise ValueError: Если изменение заряда батареи не является положительным числом
        Примеры:
        >>> phone = Phone(20, 77, False)
        >>> phone.charge(70)
        """
        if not isinstance(percentage, int):
            raise TypeError("Изменение заряда батареи должно быть типа int")
        if self.battery_level + percentage < 0 or self.battery_level + percentage > 100:
            raise ValueError("Новый уровень заряда батареи должен быть числом от 0 до 100")
        if not percentage > 0:
            raise ValueError("Изменение заряда батареи должно быть положительным числом")
        ...
    def install_app(self, app_size: Union[int, float]) -> None:
        """
        Установка приложения опредленного размера в Гб
        :param app_size: Размер приложения в Гб

        :raise ValueError: Если новая использованная память не является числом от 0 до 512 в ГБ

        :raise ValueError: Если размер приложения не является положительным числом
        Примеры:
        >>> phone = Phone(30, 248.34, False)
        >>> phone.install_app(0.023)
        """
        if not isinstance(app_size, (int, float)):
            raise TypeError("Размер приложения должен быть типа int или float")
        if self.storage_used + app_size < 0 or self.storage_used + app_size > 512:
            raise ValueError("Размер приложения должен быть числом от 0 до 512 в Гб")
        if not app_size > 0:
            raise ValueError("Размер приложения должен быть положительным числом")
        ...

class Headphones:
    def __init__(self, artist: str, song: str, is_playing: bool):
        """
        Создание и подготовка к работе объекта "Наушники"

        :param artist: Текущий исполнитель
        :param song: Текущая песня
        :param is_playing: Включена ли музыка
        Примеры:
        >>> headphones = Headphones("Linkin Park", "Lying from You", True)  # инициализация экземпляра класса
        """
        if not isinstance(artist, str):
            raise TypeError("Текущий исполнитель должен быть типа str")
        self.artist = artist

        if not isinstance(song, str):
            raise TypeError("Текущая песня должна быть типа str")
        self.song = song

        if not isinstance(is_playing, bool):
            raise TypeError("Включена ли музыка должно быть типа bool")
        self.is_playing = is_playing
    def play_pause(self) -> None:
        """
        Воспроизвести или поставить на паузу
        Примеры:
        >>> headphones = Headphones("dxntxz", "troubles", False)
        >>> headphones.play_pause()
        """
        ...
    def change_song(self, new_artist: str, new_song: str) -> None:
        """
        Смена песни в наушниках
        :param new_artist: Новый исполнитель

        :param new_song: Новая песня

        Примеры:
        >>> headphones = Headphones("2hug", "В этой комнате", True)  # инициализация экземпляра класса
        >>> headphones.change_song("xonett", "LOST")
        """
        if not isinstance(new_artist, str):
            raise TypeError("Новый исполнитель должен быть типа str")
        if not isinstance(new_song, str):
            raise TypeError("Новая песня должна быть типа str")
        ...

if __name__ == "__main__":
    doctest.testmod()# TODO работоспособность экземпляров класса проверить с помощью doctest