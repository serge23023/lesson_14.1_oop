import json
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from classes.category import Category
from classes.Products_Classes.product import Product
from classes.Products_Classes.Lawn_Grass import LawnGrass
from classes.Products_Classes.Smartphone import Smartphone


@pytest.fixture()
def mock_json_file(tmp_path):
    """
    Создаёт временный JSON-файл с корректным содержимым.

    Args:
        tmp_path (Path): Временный путь для хранения файлов.

    Returns:
        Path: Путь к созданному JSON-файлу.
    """
    data = [{"key": "value"}]
    file_path = tmp_path / "test.json"
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


@pytest.fixture()
def invalid_json_file(tmp_path):
    """
    Создаёт временный JSON-файл с некорректным содержимым.

    Args:
        tmp_path (Path): Временный путь для хранения файлов.

    Returns:
        Path: Путь к некорректному JSON-файлу.
    """
    file_path = tmp_path / "invalid.json"
    with file_path.open("w", encoding="utf-8") as f:
        f.write("{invalid_json:}")  # Некорректный JSON
    return file_path


@pytest.fixture()
def product_dict_test():
    """
    Возвращает тестовые данные продуктов.

    Returns:
        dict: Словарь с тестовыми продуктами, содержащий параметры `name`, `description`, `price` и `quantity`.
    """
    return {
        'product1': {'name': 'name', 'description': 'description', 'price': 1.0, 'quantity': 0},
        'product2': {'name': 'name', 'description': 'description', 'price': 10.0, 'quantity': 10},
        'product3': {'name': 'name', 'description': 'description', 'price': 100.0, 'quantity': 10},
        'product4': {'name': 'name1', 'description': 'description', 'price': 100.0, 'quantity': 100},
        'product5': {'name': 'name2', 'description': 'description', 'price': 100.0, 'quantity': 100}
    }.copy()


@pytest.fixture()
def categories_test(product_dict_test):
    """
    Создаёт тестовые категории, сбрасывая их счётчики перед созданием.

    Args:
        product_dict_test (dict): Тестовые данные продуктов.

    Returns:
        list[Category]: Список тестовых категорий.
    """
    Category.reset()
    return [
        Category(
            'test1',
            'description',
            [Product(**product_dict_test['product1'])])
    ].copy()


@pytest.fixture()
def lawn_grass_test():
    """
    Создаёт тестовый объект `LawnGrass`.

    Returns:
        LawnGrass: Тестовый экземпляр класса `LawnGrass`.
    """
    return LawnGrass(
        "Кентукки Блюграсс",
        "Трава для газонов",
        5,
        100,
        "USA",
        "14 дней",
        "Зеленый"
    )


@pytest.fixture()
def smartphone_test():
    """
    Создаёт тестовый объект `Smartphone`.

    Returns:
        Smartphone: Тестовый экземпляр класса `Smartphone`.
    """
    return Smartphone(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        "Флагман",
        "C23 Ultra",
        "256GB",
        "Серый"
    )
