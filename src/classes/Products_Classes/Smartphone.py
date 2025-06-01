from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class Smartphone(Product, MixinLogger):
    """Класс, представляющий смартфон как товар.

    Attributes:
        efficiency (str): Энергоэффективность.
        model (str): Модель устройства.
        memory (str): Объём встроенной памяти.
        color (str): Цвет корпуса.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ) -> None:
        """
        Инициализирует объект смартфона.

        Args:
            name (str): Название.
            description (str): Описание.
            price (float): Цена.
            quantity (int): Количество.
            efficiency (str): Энергоэффективность.
            model (str): Модель устройства.
            memory (str): Объём встроенной памяти.
            color (str): Цвет корпуса.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        if self.__class__ is Smartphone:
            self.log_creation()

    def __str__(self) -> str:
        """Упрощённое представление смартфона для пользователя."""
        return (
            f"{self.name} — {self.description}, "
            f"{self.model}, {self.memory}, {self.color}, "
            f"{self.price} руб. ({self.quantity} шт.)"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"'{self.name}', '{self.description}', {self.price}, {self.quantity}, "
            f"'{self.efficiency}', '{self.model}', '{self.memory}', '{self.color}')"
        )
