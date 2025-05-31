from classes.Order_Classes.abstract_order import AbstractOrder
from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class Order(AbstractOrder, MixinLogger):
    """Представляет заказ на товар.

    Attributes:
        product (Product): Товар, на который оформлен заказ.
        quantity (int): Количество заказанных единиц.
        total_cost (float): Общая стоимость заказа.
    """

    def __init__(self, product: Product, quantity: int) -> None:
        """
        Args:
            product (Product): Товар.
            quantity (int): Количество.

        Raises:
            ValueError: Если количество не положительное.
        """
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным.")

        self.product = product
        self.quantity = quantity
        self.total_cost = self.quantity * self.product.price

        if self.__class__ is Order:
            self.log_creation()

    def __str__(self) -> str:
        """Упрощённое представление заказа."""
        return (
            f"Заказ: {self.quantity} × {self.product.name} "
            f"на сумму {self.total_cost} руб."
        )

    def __repr__(self) -> str:
        """Техническое представление заказа."""
        return (
            f"{self.__class__.__name__}('{self.product.name}', "
            f"{self.quantity}, {self.total_cost})"
        )
