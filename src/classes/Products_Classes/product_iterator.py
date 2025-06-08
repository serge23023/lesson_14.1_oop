from classes.Products_Classes.product import Product


class ProductIterator:
    """Итератор для перебора списка товаров категории.

    Attributes:
        products (list[Product]): Список товаров.
        __index (int): Текущий индекс при итерации.
    """

    __slots__ = ("products", "__index")

    def __init__(self, products: list[Product]) -> None:
        """
        Инициализирует итератор для списка товаров.

        Args:
            products (list[Product]): Список товаров для перебора.
        """
        self.products = products
        self.__index = 0

    def __iter__(self) -> "ProductIterator":
        """
        Возвращает сам итератор (объект-итератор).

        Returns:
            ProductIterator: Текущий итератор.
        """
        self.__index = 0
        return self

    def __next__(self) -> Product:
        """
        Возвращает следующий товар из списка.

        Returns:
            Product: Следующий товар в последовательности.

        Raises:
            StopIteration: Если достигнут конец списка.
        """
        if self.__index < len(self.products):
            product = self.products[self.__index]
            self.__index += 1
            return product

        raise StopIteration
