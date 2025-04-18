class MixinLogger:
    """
    Миксин для логирования объектов.
    """

    def log_creation(self) -> None:
        """
        Логирует создание объекта.
        Выводит в консоль сообщение с техническим представлением объекта (__repr__).

        Returns:
            None
        """
        print(f"Создан объект: {self.__repr__()}\n")
