from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class LawnGrass(Product, MixinLogger):
    """Класс, представляющий газонную траву как товар.

    Attributes:
        country (str): Страна происхождения.
        germination_period (str): Период прорастания.
        color (str): Цвет травы.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """
        Инициализирует объект LawnGrass.

        Args:
            name (str): Название товара.
            description (str): Описание.
            price (float): Цена за упаковку.
            quantity (int): Количество на складе.
            country (str): Страна производства.
            germination_period (str): Период прорастания.
            color (str): Цвет травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

        if self.__class__ is LawnGrass:
            self.log_creation()

    def __str__(self) -> str:
        """Человекочитаемое представление товара."""
        return (
            f"{self.name} ({self.color}, из {self.country}) — "
            f"{self.price} руб., в наличии: {self.quantity} шт."
        )

    def __repr__(self) -> str:
        """Техническое строковое представление LawnGrass."""
        base = super().__repr__()
        return f"{base}, '{self.country}', '{self.germination_period}', '{self.color}'"
