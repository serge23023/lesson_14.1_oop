from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class Category(MixinLogger):
    """
    Класс `Category` представляет категорию товаров.

    Наследует:
        - `MixinLogger`: Миксин для логирования событий создания объекта.

    Наследует:
        - `MixinLogger`: Миксин для логирования объекта.

    Attributes:
        (класса)
        __category_count (int): Количество созданных объектов `Category`.
        __product_count (int): Количество уникальных товаров среди всех категорий.

        (экземпляра)
        __name (str): Название категории.
        __description (str): Описание категории.
        __products (list[Product]): Список товаров, принадлежащих данной категории.
    """

    __slots__ = ('__name', '__description', '__products')  # Ограничение допустимых атрибутов для оптимизации памяти.

    __category_count = 0  # Общий счетчик категорий.
    __product_count = 0  # Счетчик уникальных товаров.

    @classmethod
    @property
    def category_count(cls):
        """
        Возвращает общее количество созданных категорий.

        Returns:
            int: Количество объектов `Category`.
        """
        return cls.__category_count

    @classmethod
    @property
    def product_count(cls):
        """
        Возвращает общее количество уникальных товаров среди всех категорий.

        Returns:
            int: Общее количество уникальных товаров.
        """
        return cls.__product_count

    @classmethod
    def reset(cls):
        """
        Сбрасывает счётчики категорий и товаров до нуля.
        """
        cls.__category_count = 0
        cls.__product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """
        Инициализирует объект `Category`.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list[Product], optional): Список товаров в категории. По умолчанию — пустой список.
        """
        self.__name = name  # Название категории.
        self.__description = description  # Описание категории.
        self.__products = products if products else []  # Список товаров (или пустой список).

        Category.__category_count += 1  # Увеличение общего счётчика категорий.
        Category.__product_count += len(set(p.name for p in self.__products))  # Подсчёт уникальных товаров.

        self.log_creation()  # Логирование создания категории.


        Category.__category_count += 1
        Category.__product_count += len(set(p.name for p in self.__products))

    @property
    def products(self):
        """
        Возвращает список товаров в категории.

        Returns:
            list[Product]: Список товаров категории.
        """
        return self.__products


    @property
    def name(self) -> str:
        """
        Возвращает название категории.

        Returns:
            str: Название категории.
        """
        return self.__name

    @property
    def description(self) -> str:
        """
        Возвращает описание категории.

        Returns:
            str: Описание категории.
        """
        return self.__description

    def __len__(self):
        """
        Возвращает общее количество товаров в категории, включая их количество.

        Returns:
            int: Суммарное количество всех товаров в категории.
        """
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        """
        Возвращает строковое представление категории с количеством товаров.

        Returns:
            str: Название категории и количество товаров.
        """
        return f"\n{self.__name}, количество продуктов: {len(self)} шт."

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию, обновляя счётчик уникальных товаров.

        Args:
            product (Product): Товар для добавления.

        Raises:
            TypeError: Если переданный объект не является экземпляром `Product`.
        """
        if not isinstance(product, Product):
            raise TypeError("Должен быть объект класса Product")

        if product.name not in (p.name for p in self.__products):  # Проверка уникальности товара.
            Category.__product_count += 1

        self.__products.append(product)  # Добавление товара в список.


    def __len__(self) -> int:
        """
        Возвращает общее количество товаров в категории с учётом их количества.

        Returns:
            int: Суммарное количество единиц товаров.
        """
        count = 0
        for product in self.__products:  # Перебирает все товары в категории.
            count += product.quantity  # Суммирует количество каждого товара.
        return count

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.

        Returns:
            str: Название категории и количество товаров.
        """
        return f"\n{self.__name}, количество продуктов: {len(self)} шт."

    def __repr__(self) -> str:
        """
        Возвращает техническое представление объекта `Category`.

        Returns:
            str: Техническое представление категории для отладки.
        """
        return f"{self.__class__.__name__}('{self.__name}', '{self.__description}', {self.__products})"
