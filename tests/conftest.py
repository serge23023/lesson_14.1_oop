import os
import sys
import json
import pytest

# Добавляем src в sys.path для корректного импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from classes.Order_Classes.category import Category
from classes.Order_Classes.order import Order
from classes.Products_Classes.product import Product
from classes.Products_Classes.Smartphone import Smartphone
from classes.Products_Classes.Lawn_Grass import LawnGrass


@pytest.fixture()
def mock_json_file(tmp_path) -> str:
    """Создаёт временный корректный JSON-файл с категорией и продуктами."""
    data = [
        {
            "name": "Электроника",
            "description": "Товары электроники",
            "products": [
                {
                    "name": "iPhone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8
                }
            ]
        }
    ]
    file_path = tmp_path / "valid.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")
    return str(file_path)


@pytest.fixture()
def invalid_json_file(tmp_path) -> str:
    """Создаёт временный некорректный JSON-файл."""
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json", encoding="utf-8")
    return str(file_path)


# ----------- Продукты -----------

@pytest.fixture()
def product_iphone() -> dict:
    return {
        "name": "iPhone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    }


@pytest.fixture()
def product_samsung() -> dict:
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }


@pytest.fixture()
def product_xiaomi() -> dict:
    return {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }


# ----------- Категория -----------

@pytest.fixture()
def categories_test(product_iphone) -> Category:
    """Создаёт категорию с одним продуктом."""
    Category.reset()
    category = Category("Тестовая", "Описание", [Product(**product_iphone)])
    return category


# ----------- Специализированные товары -----------

@pytest.fixture()
def lawn_grass_test() -> LawnGrass:
    return LawnGrass(
        "Лужайка", "Описание травы", 500.0, 20, "Россия", "14 дней", "зелёный"
    )


@pytest.fixture()
def smartphone_test(product_samsung) -> Smartphone:
    data = {
        **product_samsung,
        "efficiency": "A++",
        "model": "SM-12345",
        "memory": "512GB",
        "color": "Чёрный"
    }
    return Smartphone(**data)
