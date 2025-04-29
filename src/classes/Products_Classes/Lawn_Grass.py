from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class LawnGrass(Product, MixinLogger):
    """
    Класс `LawnGrass` представляет газонную траву как продукт.

    Наследует:
        - `Product`: Базовый класс товара.
        - `MixinLogger`: Миксин для логирования событий создания объекта.

    Attributes:
        (экземпляра)
        country (str): Страна происхождения.
        germination_period (str): Период прорастания.
        color (str): Цвет травы.
    """

    __slots__ = ('country', 'germination_period', 'color')  # Оптимизация памяти.

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Инициализирует объект `LawnGrass`.

        Args:
            name (str): Название продукта.
            description (str): Описание продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта в наличии.
            country (str): Страна происхождения.
            germination_period (str): Период прорастания.
            color (str): Цвет травы.
        """
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self) -> str:
        """
        Возвращает техническое представление объекта.

        Returns:
            str: Техническое представление объекта `LawnGrass`.
        """
        return f"{Product.__repr__(self)}, '{self.country}', '{self.germination_period}', '{self.color}'"
