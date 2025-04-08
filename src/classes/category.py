from classes.mixin_log import MixinLogger
from classes.product import Product


class Category(MixinLogger):
    """
    Класс Category представляет категорию товаров.

    Наследует:
        - MixinLogger: Миксин для логирования объекта.

    Attributes:
        __category_count (int): Хранит количество созданных объектов класса Category.
        __product_count (int): Хранит количество уникальных товаров среди всех категорий.
        __name (str): Название категории.
        __description (str): Описание категории.
        __products (list[Product]): Список товаров, принадлежащих категории.
    """

    __slots__ = ('__name', '__description', '__products')  # Оптимизация памяти путем ограничения допустимых атрибутов.

    __category_count = 0  # Общий счетчик категорий.
    __product_count = 0  # Счетчик уникальных товаров.

    @classmethod
    @property
    def category_count(cls):
        """
        Возвращает количество созданных категорий.

        Returns:
            int: Количество категорий.
        """
        return cls.__category_count

    @classmethod
    @property
    def product_count(cls):
        """
        Возвращает количество уникальных товаров.

        Returns:
            int: Количество уникальных товаров.
        """
        return cls.__product_count

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """
        Инициализирует объект категории.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list[Product], optional): Список товаров. По умолчанию пустой список.
        """
        self.__name = name  # Устанавливает название категории.
        self.__description = description  # Устанавливает описание категории.
        self.__products = products if products else []  # Сохраняет список товаров или создает пустой список.
        Category.__category_count += 1  # Увеличивает счетчик категорий.
        Category.__product_count += len(set(p.name for p in self.__products))  # Подсчитывает уникальные товары.
        self.log_creation()  # Логирует создание категории.

    @property
    def products(self):
        """
        Возвращает список товаров в категории.

        Returns:
            list[Product]: Список товаров.
        """
        return self.__products

    @property
    def name(self):
        """
        Возвращает название категории.

        Returns:
            str: Название категории.
        """
        return self.__name

    @property
    def description(self):
        """
        Возвращает описание категории.

        Returns:
            str: Описание категории.
        """
        return self.__description

    def __len__(self):
        """
        Возвращает количество всех товаров в категории (с учетом их количества).

        Returns:
            int: Количество товаров.
        """
        count = 0
        for product in self.__products:  # Перебирает все товары в категории.
            count += product.quantity  # Суммирует количество каждого товара.
        return count

    def __str__(self):
        """
        Возвращает строковое представление категории.

        Returns:
            str: Строка с названием и количеством товаров.
        """
        return f"\n{self.__name}, количество продуктов: {len(self)} шт."  # Форматирует строку с данными категории.

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию и обновляет количество уникальных товаров.

        Args:
            product (Product): Товар для добавления.

        Raises:
            TypeError: Если объект не является экземпляром Product.
        """
        if not isinstance(product, Product):  # Проверяет, что добавляемый объект — это Product.
            raise TypeError("Должен быть объект класса Product")

        if product.name not in (p.name for p in self.__products):  # Если товар уникален, увеличивает счетчик.
            Category.__product_count += 1
        self.__products.append(product)  # Добавляет товар в список.

    def __repr__(self):
        """
        Возвращает техническое представление объекта категории.

        Returns:
            str: Техническая строка представления.
        """
        return f'{self.__class__.__name__}({self.__name}, {self.__description}, {self.__products})'
