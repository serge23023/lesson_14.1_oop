from classes.Order_Classes.category import Category
from classes.Products_Classes.product import Product
from read_file import open_json


def create_categories() -> list[Category]:
    """Загружает данные из JSON-файла и создаёт список объектов Category.

    Читает файл `products.json`, создаёт объекты Product и добавляет их
    в соответствующие категории через Category.add_product().

    Returns:
        list[Category]: Список категорий с добавленными товарами.

    Raises:
        FileNotFoundError: Если JSON-файл не найден.
        json.JSONDecodeError: Если содержимое некорректно.
    """
    categories: list[Category] = []

    json_data = open_json("products.json", recursive=True)

    for entry in json_data:
        product_dicts = entry.pop("products", [])
        products = [Product(**p) for p in product_dicts]
        category = Category(**entry)

        for product in products:
            category.add_product(product)

        categories.append(category)

    return categories
