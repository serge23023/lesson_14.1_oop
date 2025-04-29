class ProductIterator:
    """
    Итератор для перебора списка продуктов в категории.

    Attributes (экземпляра):
        product (list): Список товаров, доступных в категории.
        __index (int): Текущий индекс для итерации.
    """

    __slots__ = ('product', '__index')

    def __init__(self, product: list):
        """
        Инициализирует объект итератора для списка продуктов.

        Args:
            product (list): Список товаров для перебора.
        """
        self.product = product

    def __iter__(self):
        """
        Возвращает сам объект итератора.

        Returns:
            CategoryIterator: Сам итератор.
        """
        self.__index = 0
        return self

    def __next__(self):
        """
        Возвращает следующий продукт из списка.

        Returns:
            Product: Следующий товар из списка.

        Raises:
            StopIteration: Если достигнут конец списка продуктов.
        """
        if self.__index < len(self.product):
            product = self.product[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration
