from classes.mixin_log import MixinLogger
from classes.product import Product


class Category(MixinLogger):
    """
    Класс `Category` представляет категорию товаров.

    Наследует:
        - `MixinLogger`: Миксин для логирования событий создания объекта.

    Attributes:
        (класса)
        __category_count (int): Количество созданных объектов `Category`.
        __product_count (int): Количество уникальных товаров среди всех категорий.

        (экземпляра)
        __name (str): Название категории.
        __description (str): Описание категории.
        __products (list[Product]): Список товаров, принадлежащих данной категории.
    """

    __slots__ = ('__name', '__description', '__products')  # Оптимизация использования памяти.

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

        Category.__category_count += 1
        Category.__product_count += len(set(p.name for p in self.__products))

        self.log_creation()  # Логирование создания категории.

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

    @property
    def products(self) -> list[Product]:
        """
        Возвращает список товаров в данной категории.

        Returns:
            list[Product]: Список продуктов категории.
        """
        return self.__products

    def __len__(self) -> int:
        """
        Возвращает общее количество товаров в категории с учётом их количества.

        Returns:
            int: Суммарное количество единиц товаров.
        """
        return sum(product.quantity for product in self.__products)

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
            str: Представление объекта для разработчиков.
        """
        return f"{self.__class__.__name__}('{self.__name}', '{self.__description}', {self.__products})"

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию, при необходимости обновляя уже существующий.

        Args:
            product (Product): Товар для добавления.

        Raises:
            TypeError: Если объект не является экземпляром `Product`.
        """
        if not isinstance(product, Product):
            raise TypeError("Должен быть объект класса Product")

        for existing_product in self.__products:
            if product.name == existing_product.name:
                Product.edit_product(product.price, product.quantity, existing_product)
                return

        Category.__product_count += 1
        self.__products.append(product)
