# from unittest.mock import patch

import pytest

from classes.product import Product

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_product(product_dict_test):
    # Тестирование создания продукта
    key_dict = 'product1'
    product1 = Product(**product_dict_test[key_dict])
    assert isinstance(product1, Product)  # Проверка типа объекта
    assert product1.name == product_dict_test[key_dict]['name']  # Проверка имени
    assert product1.description == product_dict_test[key_dict]['description']  # Проверка описания
    assert product1.price == product_dict_test[key_dict]['price']  # Проверка цены
    assert product1.quantity == product_dict_test[key_dict]['quantity']  # Проверка количества
