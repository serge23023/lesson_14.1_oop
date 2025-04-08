import pytest

from classes.category import Category
from classes.product import Product

if __name__ == '__main__':
    pytest.main()


def test_category(categories_test, product_dict_test):
    category1 = categories_test[0]

    # Проверяем категорию
    assert isinstance(category1, Category)
    assert category1.name == 'test1'
    assert category1.description == 'description'
    assert isinstance(category1.products, list)
    assert isinstance(category1.products[0], Product)
    assert len(category1) == 0
    assert str(category1) == f"\ntest1, количество продуктов: {len(category1)} шт."

    # Проверяем общее количество категорий и уникальных продуктов
    assert Category.category_count == 1
    assert Category.product_count == 1
    print("______---------")
    print(category1.products)

    # Добавляем новую категорию и проверяем общее количество категорий
    category2 = Category('test2', 'description')
    categories_test.append(category2)
    assert Category.category_count == 2


def test_add_product(categories_test, product_dict_test):
    category = categories_test[0]

    # Добавляем продукты в категорию и проверяем общее количество уникальных продуктов и его наличие в списке продуктов
    new_product = Product(**product_dict_test['product4'])
    category.add_product(new_product)
    assert Category.product_count == 2
    assert any(product.name == new_product.name for product in category.products)

    # Добавляем продукт, который уже существует, и проверяем общее количество уникальных продуктов
    category.add_product(new_product)
    assert Category.product_count == 2

    # Добавляем продукт с новым именем и проверяем общее количество уникальных продуктов
    new_unique_product = Product(**product_dict_test['product5'])
    category.add_product(new_unique_product)
    assert Category.product_count == 3

    # Добавляем объект тип которого не class Product или его наследник
    with pytest.raises(TypeError):
        category.add_product("Not a product")


# def test_average_price(categories_test):
#     category = categories_test[0]
#     assert category.average_price() == 1.0
#     category.products.remove(category.products[0])
#     assert category.average_price() == 0
