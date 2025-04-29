from classes.category import Category
from classes.Products_Classes.product import Product
from read_file import open_json


def create_categories():
    """
    Загружает данные из JSON-файла и создаёт список объектов `Category`.

    Функция открывает файл `products.json`, извлекает данные, создаёт объекты `Product` для товаров
    и добавляет их в соответствующие категории.

    Returns:
        list[Category]: Список объектов `Category` с загруженными товарами.
    """
    categories = []

    for item in open_json('products.json', True):  # Чтение данных из JSON-файла
        products = [Product(**product) for product in item.pop('products', [])]  # Создаём объекты `Product`
        category = Category(**item)  # Создаём объект `Category`

        for product in products:
            category.add_product(product)  # Добавляем товары в категорию

        categories.append(category)

    return categories
