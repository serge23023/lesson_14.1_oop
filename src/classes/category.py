from classes.mixin_log import MixinCreationLogger
from classes.product import Product


class Category(MixinCreationLogger):
    """
    Класс Category представляет категорию товаров.

    Атрибуты класса:
        __category_count (int): Хранит количество созданных объектов класса Category.
        __product_count (int): Хранит количество уникальных товаров среди всех категорий.

    Атрибуты экземпляра:
        __name (str): Название категории.
        __description (str): Описание категории.
        __products (list[Product]): Список товаров, принадлежащих категории.

    Методы класса:
        category_count: Возвращает количество созданных категорий.
        product_count: Возвращает количество уникальных товаров.
        reset: Сбрасывает счетчики категорий и товаров.
    """

    __slots__ = ('__name', '__description', '__products')

    __category_count = 0
    __product_count = 0

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

    @classmethod
    def reset(cls):
        """
        Сбрасывает счетчики категорий и товаров.
        """
        cls.__category_count = 0
        cls.__product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """
        Инициализирует объект категории.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list[Product], optional): Список товаров. По умолчанию пустой список.
        """
        self.__name = name
        self.__description = description
        self.__products = products if products else []
        Category.__category_count += 1
        Category.__product_count += len(set(p.name for p in self.__products))
        self.log_creation()

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
        for product in self.__products:
            count += product.quantity
        return count

    def __str__(self):
        """
        Возвращает строковое представление категории.

        Returns:
            str: Строка с названием и количеством товаров.
        """
        return f"\n{self.__name}, количество продуктов: {len(self)} шт."

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию и обновляет количество уникальных товаров.

        Args:
            product (Product): Товар для добавления.

        Raises:
            TypeError: Если объект не является экземпляром Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Должен быть объект класса Product")

        if product.name not in (p.name for p in self.__products):
            Category.__product_count += 1
        self.__products.append(product)

    def average_price(self):
        """
        Вычисляет среднюю цену товаров в категории.

        Returns:
            float: Средняя цена товаров. Возвращает 0, если список товаров пуст.
        """
        total_price = 0
        for product in self.__products:
            total_price += product.price
        try:
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __repr__(self):
        """
        Возвращает техническое представление объекта категории.

        Returns:
            str: Техническая строка представления.
        """
        return f'{self.__class__.__name__}({self.__name}, {self.__description}, {self.__products})'
