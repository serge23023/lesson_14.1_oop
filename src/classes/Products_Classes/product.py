from classes.Products_Classes.abstact_product import BaseProduct
from classes.mixin_log import MixinLogger


class Product(BaseProduct, MixinLogger):
    """Базовый класс товара.

    Attributes:
        name (str): Название товара.
        description (str): Описание товара.
        quantity (int): Количество на складе.
        __price (float): Цена товара (через @property).
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализирует новый товар.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Начальная цена.
            quantity (int): Начальное количество на складе.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        if self.__class__ is Product:
            self.log_creation()

    def update(self, price: float, quantity: int) -> None:
        """
        Обновляет цену и увеличивает количество.

        Args:
            price (float): Новая цена.
            quantity (int): Количество, которое нужно добавить.

        Raises:
            ValueError: Если цена не положительная.
        """
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        self.__price = price
        self.quantity += quantity

    @property
    def price(self) -> float:
        """Текущая цена товара."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает новую цену товара.

        Args:
            value (float): Новая цена.

        Raises:
            ValueError: Если значение не положительное.

        Notes:
            - При понижении цены требуется подтверждение.
            - При повышении — цена устанавливается без подтверждения.
        """
        if value <= 0:
            print("Ошибка: Цена не должна быть нулевой или отрицательной.")
        elif value < self.__price:
            confirm = input(
                f"Новая цена ниже текущей ({self.__price} → {value}).\n"
                'Введите "y" для подтверждения: '
            )
            if confirm == "y":
                self.__price = value
            else:
                print("Понижение цены отменено.")
        else:
            self.__price = value

    def __add__(self, other: "Product") -> float:
        """
        Складывает стоимость двух товаров.

        Args:
            other (Product): Второй товар.

        Returns:
            float: Общая стоимость двух товаров.

        Raises:
            TypeError: Если объект не является Product.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только товары одного типа.")
        return self.price * self.quantity + other.price * other.quantity

    def __eq__(self, other: object) -> bool:
        """
        Сравнивает товары по имени и цене.

        Args:
            other (object): Второй объект.

        Returns:
            bool: True, если имя и цена совпадают.
        """
        return (
                isinstance(other, Product)
                and self.name == other.name
                and self.price == other.price
        )

    def __str__(self) -> str:
        """Человекочитаемое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """Техническое строковое представление товара."""
        return (
            f"{self.__class__.__name__}('{self.name}', "
            f"'{self.description}', {self.price}, {self.quantity})"
        )
