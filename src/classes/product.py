from classes.mixin_log import MixinCreationLogger
from classes.abstact_product import AbstractProduct


class Product(AbstractProduct, MixinCreationLogger):
    """
    Класс Product представляет товар с именем, описанием, ценой и количеством.
    Реализует методы для создания товара, работы с ценой и выполнения арифметических операций.
    Наследует:
    - AbstractProduct: Базовый абстрактный класс.
    - MixinCreationLogger: Миксин для логирования создания объекта.
    """

    # Использование __slots__ для ограничения атрибутов объекта и оптимизации памяти
    __slots__ = ('name', 'description', '__price', 'quantity')

    @classmethod
    def create_product(cls, new_product: dict, product_list: list = None):
        """
        Создает новый объект Product или обновляет существующий в списке товаров.

        Args:
            new_product (dict): Словарь с данными нового товара (name, description, price, quantity).
            product_list (list, optional): Список существующих объектов Product. Defaults to None.

        Returns:
            Product: Новый или обновленный объект Product.

        Raises:
            Возвращает None, если товар обновлен в списке существующих товаров.
        """
        if product_list is None:
            product_list = []

        for product in product_list:
            if product.name == new_product['name']:
                # Найден товар с таким же именем
                if product.price >= new_product['price']:
                    # Если текущая цена выше, используем ее
                    product.quantity += new_product['quantity']
                    return
                else:
                    # Если новая цена выше, обновляем цену и количество
                    product.price = new_product['price']
                    product.quantity += new_product['quantity']
                    return
        # Если товар уникален, создаем новый объект
        return cls(**new_product)

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализирует объект Product.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество товара.
        """
        self.name = name
        self.description = description
        self.__price = price  # Установка цены через внутренний атрибут
        self.quantity = quantity
        self.log_creation()  # Логирует создание объекта

    @property
    def price(self):
        """
        Возвращает текущую цену товара.

        Returns:
            float: Цена товара.
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Устанавливает новую цену товара. Требует подтверждение при снижении цены.

        Args:
            value (float): Новая цена товара.

        Raises:
            ValueError: Если цена меньше или равна 0.
        """
        if value <= 0:
            raise ValueError("Введена некорректная цена")
        elif value < self.__price:
            # Подтверждение снижения цены
            if input(f'Цена после подтверждения: {value} руб.\nВведите "y" для подтверждения понижения цены:') == 'y':
                self.__price = float(value)
        else:
            self.__price = float(value)

    def __str__(self):
        """
        Возвращает строковое представление объекта Product.

        Returns:
            str: Информация о товаре (название, цена, количество).
        """
        return f"\n{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение стоимости двух объектов Product.

        Args:
            other (Product): Другой объект Product.

        Returns:
            float: Общая стоимость двух товаров.

        Raises:
            TypeError: Если другой объект не является экземпляром Product.
        """
        if type(self) is not type(other):
            raise TypeError
        return self.__price * self.quantity + other.__price * other.quantity

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.

        Returns:
            str: Конструктор объекта в виде строки.
        """
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
