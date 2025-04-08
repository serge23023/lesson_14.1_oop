import json
import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from classes.category import Category
from classes.product import Product


@pytest.fixture()
def mock_json_file(tmp_path):
    # Создаем временный JSON-файл с корректным содержимым
    data = [{"key": "value"}]
    file_path = tmp_path / "test.json"
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f)
    return file_path


@pytest.fixture()
def invalid_json_file(tmp_path):
    # Создаем временный JSON-файл с некорректным содержимым
    file_path = tmp_path / "invalid.json"
    with file_path.open("w", encoding="utf-8") as f:
        f.write("{invalid_json:}")  # Некорректный JSON
    return file_path


@pytest.fixture()
def product_dict_test():
    return {
        'product1': {'name': 'name', 'description': 'description', 'price': 1.0, 'quantity': 0},
        'product2': {'name': 'name', 'description': 'description', 'price': 10.0, 'quantity': 10},
        'product3': {'name': 'name', 'description': 'description', 'price': 100.0, 'quantity': 10},
        'product4': {'name': 'name1', 'description': 'description', 'price': 100.0, 'quantity': 100},
        'product5': {'name': 'name2', 'description': 'description', 'price': 100.0, 'quantity': 100}
    }.copy()


@pytest.fixture()
def categories_test(product_dict_test):
    Category.reset()
    return [
        Category(
            'test1',
            'description',
            [Product(**product_dict_test['product1'])])
    ].copy()

# @pytest.fixture()
# def categories_test(product_dict_test):
#     Category.reset()
#     return [
#         Category(
#             'test1',
#             'description',
#             [Product.new_product(product_dict_test['product1'])])
#     ].copy()
