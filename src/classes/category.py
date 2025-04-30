from classes.product import Product


class Category:
    """
    Класс Category представляет категорию товаров.

    Атрибуты класса:
        category_count (int): Хранит количество созданных объектов класса Category.
        product_count (int): Хранит количество уникальных товаров среди всех категорий.

    Атрибуты экземпляра:
        name (str): Название категории.
        description (str): Описание категории.
        products (list[Product]): Список товаров, принадлежащих категории.
    """

    __slots__ = ('name', 'description', 'products')

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """
        Инициализирует объект категории.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list[Product], optional): Список товаров. По умолчанию пустой список.
        """
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(set(p.name for p in self.products))
