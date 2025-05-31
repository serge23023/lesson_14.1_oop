from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех типов товаров.

    Определяет обязательные методы, которые должен реализовать
    любой конкретный продукт (например, Smartphone, LawnGrass).

    Methods:
        __init__(): Инициализация продукта.
        __add__(other): Сложение стоимости двух товаров.
        __str__(): Человекочитаемое строковое представление.
        __repr__(): Техническое строковое представление.
        update(price, quantity): Обновление цены и количества.
    """

    @abstractmethod
    def __init__(self):
        """Инициализация продукта."""
        pass  # pragma: no cover

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Сложение стоимости двух товаров.

        Args:
            other (BaseProduct): Другой товар.

        Returns:
            float: Общая стоимость обоих товаров.

        Raises:
            TypeError: Если передан объект несовместимого типа.
        """
        pass  # pragma: no cover

    @abstractmethod
    def __str__(self) -> str:
        """Человекочитаемое строковое представление.

        Returns:
            str: Название, цена, остаток.
        """
        pass  # pragma: no cover

    @abstractmethod
    def __repr__(self) -> str:
        """Техническое строковое представление объекта.

        Returns:
            str: Строка с полными данными объекта.
        """
        pass  # pragma: no cover

    @abstractmethod
    def update(self, price: float, quantity: int) -> None:
        """Обновляет цену и количество товара.

        Args:
            price (float): Новая цена.
            quantity (int): Изменение количества.
        """
        pass  # pragma: no cover
