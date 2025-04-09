class Product():
    """
    Класс Product представляет товар с именем, описанием, ценой и количеством.
    """

    # Использование __slots__ для ограничения атрибутов объекта и оптимизации памяти
    __slots__ = ('name', 'description', '__price', 'quantity')

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

    @property
    def price(self):
        """
        Возвращает текущую цену товара.

        Returns:
            float: Цена товара.
        """
        return self.__price

    def __str__(self):
        """
        Возвращает строковое представление объекта Product.

        Returns:
            str: Информация о товаре (название, цена, количество).
        """
        return f"\n{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        """
        Возвращает строковое представление объекта для разработчиков.

        Returns:
            str: Конструктор объекта в виде строки.
        """
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"
