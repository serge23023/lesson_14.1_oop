class Product:
    """
    Класс Product представляет товар с именем, описанием, ценой и количеством.
    """

    # Использование __slots__ для ограничения атрибутов объекта и оптимизации памяти
    __slots__ = ('name', 'description', 'price', 'quantity')

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
        self.price = price  # Установка цены через внутренний атрибут
        self.quantity = quantity
