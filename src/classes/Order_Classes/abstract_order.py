from abc import ABC, abstractmethod


class AbstractOrder(ABC):
    """
    Абстрактный базовый класс для объектов заказа.

    Требует реализации методов строкового представления и инициализации.
    """

    @abstractmethod
    def __init__(self):
        """
        Инициализация объекта.

        Должна быть реализована в подклассах.
        """
        pass  # pragma: no cover

    @abstractmethod
    def __repr__(self) -> str:
        """
        Возвращает техническое строковое представление объекта (для отладки).

        Returns:
            str: Подробная строка, содержащая внутренние данные объекта.
        """
        pass  # pragma: no cover

    @abstractmethod
    def __str__(self) -> str:
        """
        Возвращает человекочитаемое строковое представление объекта.

        Returns:
            str: Упрощённая строка для отображения пользователю.
        """
        pass  # pragma: no cover
