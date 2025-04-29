from classes.category import Category
from classes.product import Product
from read_file import open_json


def create_categories():
    """
    Загружает данные из JSON-файла и создаёт список объектов `Category`.

    Функция открывает файл `products.json`, извлекает данные, создаёт объекты `Product` для товаров
    и добавляет их в соответствующие категории.

    Returns:
        list[Category]: Список объектов `Category` с загруженными товарами.
    """
    categories = []  # Инициализация списка категорий
    for item in open_json('products.json', True):  # Чтение данных из JSON-файла
        # Создание объектов Product для каждого товара в категории
        item['products'] = [Product(**product) for product in item['products']]
        # Создание объекта Category и добавление его в список категорий
        categories.append(Category(**item))
    return categories  # Возвращает список категорий с товарами
