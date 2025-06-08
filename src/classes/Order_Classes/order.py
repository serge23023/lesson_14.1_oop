from classes.Order_Classes.abstract_order import AbstractOrder
from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product
from classes.exceptions import InvalidQuantityException


class Order(AbstractOrder, MixinLogger):
    """Представляет заказ на товар.

    Attributes:
        product (Product): Товар, на который оформлен заказ.
        quantity (int): Количество заказанных единиц.
        total_cost (float): Общая стоимость заказа.
    """

    def __init__(self, product, quantity):
        """
        Инициализация заказа на продукт с заданным количеством.

        Args:
            product (Product): Продукт для заказа.
            quantity (int): Количество заказываемого товара.

        Raises:
            InvalidQuantityException: Если quantity <= 0
        """
        try:
            if quantity <= 0:
                raise InvalidQuantityException()
        except InvalidQuantityException as e:
            print(e)
        else:
            self.product = product
            self.quantity = quantity
            self.total_cost = self.quantity * self.product.price
            self.log_creation()
            print("Товар добавлен")
        finally:
            print("Обработка оформления заказа завершена")

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
