if __name__ == "__main__":
    class Artist:
        def __init__(self, name: str, monthly_listeners: float, genre: str):
            """
            Создание и подготовка к работе объекта "Исполнитель"

            :param name: имя/псевдоним
            :param monthly_listeners: количество слушателей за месяц в тысячах (инкапсулирован, так как обновляется администратором стримингового сервиса)
            :param genre: жанр

            Примеры:
            >>> artist = Artist("John Williams", 336, "Orchestral")  # инициализация экземпляра класса
            """
            if not isinstance(name, str):
                raise TypeError("Имя должно быть строкой")
            if not isinstance(monthly_listeners, (int, float)):
                raise TypeError("Количество слушателей должно быть числом")
            if monthly_listeners < 0:
                raise ValueError("Количество слушателей не может быть отрицательным")
            if not isinstance(genre, str):
                raise TypeError("Жанр должен быть строкой")

            self.name = name
            self._monthly_listeners = monthly_listeners
            self.genre = genre

        def get_monthly_listeners(self) -> float:
            """
            Функция которая возвращает количество слушателей за месяц в тысячах

            :return: количество слушателей за месяц в тысячах

            Примеры:
            >>> artist = Artist("Corey Taylor", 899.2, "Metal")
            >>> artist.get_monthly_listeners()
            """
            return self._monthly_listeners

        def __str__(self) -> str:
            """
            Метод строкового представления исполнителя.

            :return: пользовательское описание исполнителя

            Примеры:
            >>> artist = Artist("Corey Taylor", 899.2, "Metal")
            >>> print(artist)
            """
            return f"{self.name} - исполнитель жанра {self.genre}, имеет {self._monthly_listeners} тысяч слушателей в этом месяце."

        def __repr__(self) -> str:
            """
            Метод технического представления.

            :return: техническое представление для разработчиков

            Примеры:
            >>> artist = Artist("Corey Taylor", 899.2, "Metal")
            >>> repr(artist)
            """
            return f"{self.__class__.__name__}(name={self.name!r}, monthly_listeners={self._monthly_listeners!r}, genre={self.genre!r})"

    class Band(Artist):
        def __init__(self, name: str, monthly_listeners: float, genre: str, members: list, is_active: bool):
            """
            Создание и подготовка к работе объекта "Группа"

            :param name: название группы
            :param monthly_listeners: количество слушателей за месяц в тысячах (инкапсулирован, так как обновляется администратором стримингового сервиса)
            :param genre: жанр
            :param members: список участников группы
            :param is_active: является ли группа действующей (инкапсулирован, так как обновляется администратором стримингового сервиса)

            Примеры:
            >>> band = Band("Linkin Park", 4262, "Metal", ["Chester Bennington", "Mike Shinoda"], True)  # инициализация экземпляра класса
            """

            super().__init__(name, monthly_listeners, genre)

            if not isinstance(members, list):
                raise TypeError("Участники должны быть списком")
            if not all(isinstance(m, str) for m in members):
                raise TypeError("Каждый участник должен быть строкой")

            self.members = members
            self._is_active = is_active

        def add_member(self, new_member: str) -> None:
            """
            Функция которая добавляет участника в группу

            :param new_member: имя нового участника

            Примеры:
            >>> band = Band("Linkin Park", 4262, "Metal", ["Chester Bennington", "Mike Shinoda"], True)
            >>> band.add_member("Emily Armstrong")
            """
            if not isinstance(new_member, str):
                raise TypeError("Имя участника должно быть строкой")
            self.members.append(new_member)

        def get_monthly_listeners(self) -> float:
            """
            Перегруженный метод получения количества слушателей.

            Причина перегрузки: у группы своя отдельная карточка в стриминговом сервисе,
            где количество слушателей считается отдельно от сольных исполнителей.
            Даже если у солиста 500к слушателей, у его группы может быть 2 млн.

            :return: количество слушателей группы в тысячах
            """
            return self._monthly_listeners

        @property
        def is_active(self) -> bool:
            return self._is_active

        def __str__(self) -> str:
            """
            Перегруженный метод строкового представления группы.

            Причина перегрузки: группа должна показывать не только базовую информацию
            (название, жанр, слушатели), но и количество участников, а также статус активности.
            У сольного исполнителя этой информации нет.

            :return: пользовательское описание группы

            Примеры:
            >>> band = Band("Linkin Park", 4262, "Metal", ["Chester Bennington", "Mike Shinoda"], True)
            >>> print(band)
            """
            status = "активна" if self._is_active else "неактивна"
            return (f"{self.name} - группа в жанре {self.genre}, имеет {self._monthly_listeners} тысяч слушателей. "
                    f"В составе {len(self.members)} участников, {status}.")
