from classes.Order_Classes.abstract_order import AbstractOrder
from classes.mixin_log import MixinLogger
from classes.Products_Classes.product import Product


class Category(AbstractOrder, MixinLogger):
    """Категория товаров.

    Attributes:
        __name (str): Название категории.
        __description (str): Описание категории.
        __products (list[Product]): Список товаров в категории.

        (Class)
        __category_count (int): Общее количество созданных категорий.
        __product_count (int): Количество уникальных товаров во всех категориях.
    """

    __slots__ = ("__name", "__description", "__products")

    __category_count = 0
    __product_count = 0

    @classmethod
    @property
    def category_count(cls) -> int:
        """Количество созданных категорий."""
        return cls.__category_count

    @classmethod
    @property
    def product_count(cls) -> int:
        """Общее количество уникальных товаров."""
        return cls.__product_count

    @classmethod
    def reset(cls) -> None:
        """Сбрасывает счётчики категорий и товаров."""
        cls.__category_count = 0
        cls.__product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        """
        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list[Product], optional): Список товаров (по умолчанию — пустой).
        """
        self.__name = name
        self.__description = description
        self.__products = products or []

        Category.__category_count += 1
        Category.__product_count += len({p.name for p in self.__products})

        self.log_creation()

    @property
    def name(self) -> str:
        """Название категории."""
        return self.__name

    @property
    def description(self) -> str:
        """Описание категории."""
        return self.__description

    @property
    def products(self) -> list[Product]:
        """Список товаров в категории."""
        return self.__products

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию или обновляет существующий.

        Args:
            product (Product): Товар для добавления.

        Raises:
            TypeError: Если передан не Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Ожидается объект класса Product")

        for existing_product in self.__products:
            if product.name == existing_product.name:
                existing_product.update(product.price, product.quantity)
                return

        Category.__product_count += 1
        self.__products.append(product)

    def __len__(self) -> int:
        """Общее количество единиц товаров в категории."""
        return sum(p.quantity for p in self.__products)

    def __str__(self) -> str:
        """Человекочитаемое представление категории."""
        return (
            f"{self.__name} — {self.__description}, "
            f"{len(self)} ед. (уникальных товаров: {len(self.__products)})"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"'{self.name}', '{self.description}', {repr(self.products)})"
        )
