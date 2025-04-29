import pytest

from classes.category import Category
from utils import create_categories  # from utils import create_categories, add_product

if __name__ == '__main__':
    pytest.main()


def test_create_categories():
    """
    Тестирование функции `create_categories`.

    Assertions:
        - Проверка, что каждый созданный объект является экземпляром `Category`.
    """
    assert all(isinstance(category, Category) for category in create_categories())

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
