from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class Smartphone(Product, MixinLogger):
    """
    Класс `Smartphone` представляет собой конкретный товар — смартфон,
    унаследованный от класса `Product` и `MixinLogger`.

    Наследует:
        - `Product`: Базовый класс товара с общими атрибутами.
        - `MixinLogger`: Миксин для логирования объекта.

    Attributes:
        (экземпляра)
        efficiency (str): Энергоэффективность смартфона.
        model (str): Модель смартфона.
        memory (str): Объём встроенной памяти.
        color (str): Цвет устройства.
    """

    __slots__ = ('efficiency', 'model', 'memory', 'color')  # Оптимизация использования памяти.

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """
        Инициализирует объект `Smartphone`.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество товара.
            efficiency (str): Энергоэффективность устройства.
            model (str): Модель смартфона.
            memory (str): Объём встроенной памяти.
            color (str): Цвет корпуса.
        """
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        """
        Возвращает техническое представление объекта.

        Returns:
            str: Представление объекта для разработчиков с учётом специфичных атрибутов смартфона.
        """
        return f"{Product.__repr__(self)}, '{self.efficiency}', '{self.model}', '{self.memory}', '{self.color}'"
