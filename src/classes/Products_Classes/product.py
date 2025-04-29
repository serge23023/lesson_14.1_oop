<<<<<<<< HEAD:src/classes/product.py
========
from classes.mixin_log import MixinLogger


class Product(MixinLogger):
    """
    Класс `Product` описывает товар с основными атрибутами и методами для работы с ним.

    Наследует:
        - `MixinLogger`: Миксин для логирования объекта.

    Attributes:
        (экземпляра)
        name (str): Название товара.
        description (str): Описание товара.
        __price (float): Цена товара.
        quantity (int): Количество товара.
    """

    __slots__ = ('name', 'description', '__price', 'quantity')  # Оптимизация памяти.

    @classmethod
    def edit_product(cls, price: float, quantity: int, product: 'Product') -> None:
        """
        Обновляет цену и количество товара.

        Args:
            price (float): Новая цена товара.
            quantity (int): Количество для увеличения.
            product (Product): Объект товара для редактирования.

        Notes:
            - Цена устанавливается через соответствующий сеттер.
            - Количество увеличивается на переданное значение.
        """
        product.price = price  # Используем сеттер для обновления цены.
        product.quantity += quantity  # Обновляем количество товара.

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует объект `Product`.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество товара.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.log_creation()  # Логируем создание объекта.

    @property
    def price(self) -> float:
        """
        Возвращает текущую цену товара.

        Returns:
            float: Цена товара.
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает новую цену товара.

        Args:
            value (float): Новая цена товара.

        Raises:
            ValueError: Если `value` отрицательное или равно нулю.

        Notes:
            - При попытке понизить цену запрашивается подтверждение от пользователя.
            - Если цена валидна и выше текущей, устанавливается автоматически.
        """
        if value <= 0:
            print("Ошибка: Цена не должна быть нулевой или отрицательной.")
        elif value < self.__price:  # Если новая цена ниже текущей, требуется подтверждение.
            if input(f'Цена после подтверждения: {value} руб.\nВведите "y" для подтверждения понижения цены:') == 'y':
                self.__price = value  # Устанавливаем новую цену после подтверждения.
        else:
            self.__price = value  # Устанавливаем новую цену без подтверждения.

    def __add__(self, other: 'Product') -> float:
        """
        Складывает общую стоимость двух товаров.

        Операция сложения вычисляет общую стоимость всех единиц товара,
        умножая цену каждого продукта на его количество и суммируя результаты.

        Args:
            other (Product): Второй объект `Product`.

        Raises:
            TypeError: Если передан объект, который не является `Product`.

        Returns:
            float: Общая стоимость (`price * quantity`) двух товаров.
        """
        if not isinstance(other, Product) or not issubclass(type(other), type(self)):
            raise TypeError("Операция сложения поддерживается только для объектов `Product` или его подклассов.")

        return self.__price * self.quantity + other.__price * other.quantity

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Название товара, его цена и остаток.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """
        Возвращает техническое представление объекта.

        Returns:
            str: Представление объекта для разработчиков.
        """
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
