import pytest

from classes.Products_Classes.product import Product
from classes.category import Category
from utils import create_categories

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_create_categories_returns_categories():
    """Проверяет, что функция возвращает экземпляры Category."""
    categories = create_categories()
    assert all(isinstance(cat, Category) for cat in categories)


def test_add_product_updates_category_and_count(categories_test):
    """
    Проверяет добавление продукта в категорию:
        - категория остаётся на месте,
        - глобальный счётчик продуктов увеличивается,
        - продукт добавлен в список продуктов категории.
    """
    test_category = categories_test[0]
    product_count_before = Category.product_count
    category_products_before = len(test_category.products)

    test_product = Product(
        name="Test Product",
        description="Test description",
        price=100.0,
        quantity=5
    )

    test_category.add_product(test_product)

    assert Category.category_count == len(categories_test)
    assert Category.product_count == product_count_before + 1
    assert len(test_category.products) == category_products_before + 1
    assert test_category.products[-1] == test_product
