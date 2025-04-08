from classes.category import Category
from classes.product import Product
from read_file import open_json


def create_categories():
    """
    Создает список объектов Category из данных JSON-файла.

    Открывает файл 'products.json', извлекает данные, создает объекты Product для товаров
    и добавляет их в соответствующие категории.

    Returns:
        list[Category]: Список объектов категории.
    """
    categories = []  # Инициализация списка категорий
    for item in open_json('products.json', True):  # Чтение данных из JSON-файла
        # Создание объектов Product для товаров в категории
        item['products'] = [Product(**product) for product in item['products']]
        # Создание объекта Category и добавление в список
        categories.append(Category(**item))
    return categories  # Возврат списка категорий
