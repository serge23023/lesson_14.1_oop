from typing import Optional
from classes.mixin_log import MixinLogger


class Product(MixinLogger):
    """
    Класс Product описывает товар с основными атрибутами и методами для работы с ним.

    Наследует:
        - MixinLogger: Миксин для логирования объекта.

    Attributes:
        name (str): Название товара.
        description (str): Описание товара.
        __price (float): Цена товара.
        quantity (int): Количество товара.
    """

    # Оптимизация памяти: ограничиваем атрибуты экземпляра только перечисленными
    __slots__ = ('name', 'description', '__price', 'quantity')

    @classmethod
    def new_product(cls, product_data: dict, product_list: Optional[list] = None) -> Optional['Product']:
        """
        Создаёт новый объект Product или обновляет существующий объект в списке.

        Args:
            product_data (dict): Данные товара (имя, описание, цена, количество).
            product_list (list, optional): Список существующих товаров. Defaults to None.

        Returns:
            Optional[Product]: Новый объект Product или None, если товар обновлён.
        """
        if product_list is None:
            product_list = []  # Инициализация пустого списка, если он не указан.

        for product in product_list:
            if product.name == product_data['name']:  # Проверка на совпадение имени товара.
                product.price = product_data['price']  # Используем сеттер для обновления цены.
                product.quantity += product_data['quantity']  # Обновляем количество товара.
                return None  # Возвращаем None, если обновили существующий товар.
        return cls(**product_data)  # Создаем новый товар, если он уникален.

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует объект товара.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество товара.

        Returns:
            None
        """
        self.name = name
        self.description = description
        self.__price = price  # Установка цены через внутренний атрибут
        self.quantity = quantity
        self.log_creation()  # Логируем создание объекта через миксин.

    @property
    def price(self) -> float:
        """
        Возвращает текущую цену товара.

        Returns:
            float: Цена товара.
        """
        return self.__price  # Получаем текущую цену через геттер.

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает новую цену товара.

        Args:
            value (float): Новая цена товара.

        Returns:
            None
        """
        if value <= 0:
            print("Ошибка: Цена не должна быть нулевой или отрицательной.")
        elif value < self.__price:  # Если новая цена ниже текущей, требуется подтверждение.
            if input(f'Цена после подтверждения: {value} руб.\nВведите "y" для подтверждения понижения цены:') == 'y':
                self.__price = value  # Устанавливаем новую цену после подтверждения.
        else:
            self.__price = value  # Устанавливаем новую цену без подтверждения.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.

        Returns:
            str: Название товара, его цена и остаток.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."  # Удобный вывод для пользователя.

    def __repr__(self) -> str:
        """
        Возвращает техническое представление объекта.

        Returns:
            str: Представление объекта для разработчиков.
        """
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
