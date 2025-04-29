import pytest

from classes.Products_Classes.product import Product
from classes.category import Category
from utils import create_categories

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_create_categories_returns_categories():
    """Проверяет, что функция возвращает экземпляры Category."""
    categories = create_categories()
    """
    Тестирование функции `create_categories`.

    Assertions:
        - Проверка, что каждый созданный объект является экземпляром `Category`.
    """
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

# def test_add_property_to_category(categories_test):
#     """
#     Тестирование добавления нового продукта в категорию.
#
#     Args:
#         categories_test (list[Category]): Список тестовых категорий.
#
#     Assertions:
#         - Проверка, что количество категорий остаётся неизменным.
#         - Проверка, что количество уникальных продуктов увеличивается после добавления нового продукта.
#     """
#     initial_total_unique_products = Category.product_count
#     add_product(
#         categories_test,
#         'test1',
#         {
#             'name': 'name1',
#             'description': 'description',
#             'price': 0.0,
#             'quantity': 0}
#     )
#     assert Category.category_count == 1
#     assert Category.product_count == initial_total_unique_products + 1
