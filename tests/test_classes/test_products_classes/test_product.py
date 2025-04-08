from unittest.mock import patch

import pytest

from classes.product import Product

if __name__ == '__main__':
    pytest.main()


def test_product(product_dict_test):
    # Тестирование создания продукта
    key_dict = 'product1'
    product1 = Product(**product_dict_test[key_dict])
    expected_repr = f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт."
    assert str(product1) == expected_repr  # Проверка строкового представления
    assert isinstance(product1, Product)  # Проверка типа объекта
    assert product1.name == product_dict_test[key_dict]['name']  # Проверка имени
    assert product1.description == product_dict_test[key_dict]['description']  # Проверка описания
    assert product1.price == product_dict_test[key_dict]['price']  # Проверка цены
    assert product1.quantity == product_dict_test[key_dict]['quantity']  # Проверка количества


# def test_add_product(product_dict_test):
#     # Тестирование сложения объектов между собой
#     key_dict1 = 'product2'
#     key_dict2 = 'product3'
#     product1 = Product(**product_dict_test[key_dict1])
#     product2 = Product(**product_dict_test[key_dict2])
#     assert product1 + product2 == 1100.0
#
#     with pytest.raises(TypeError):
#         product1 + "Not a product"


def test_create_product_new_price(product_dict_test):
    # Тестирование создания нового продукта с обновлением цены
    key_dict1 = 'product1'
    key_dict2 = 'product2'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product.new_product(product_dict_test[key_dict2], [product1])
    assert isinstance(product2, type(None))  # Ожидается, что новый продукт не будет создан
    assert product1.price == product_dict_test[key_dict2]['price']  # Проверка обновления цены
    assert product1.quantity == product_dict_test[key_dict2]['quantity']  # Проверка обновления количества


def test_create_product_existing_price(product_dict_test):
    # Тестирование создания нового продукта с существующей ценой
    key_dict1 = 'product3'
    key_dict2 = 'product2'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product.new_product(product_dict_test[key_dict1], [product1])
    assert isinstance(product2, type(None))  # Ожидается, что новый продукт не будет создан
    assert product1.price == product_dict_test[key_dict1]['price']  # Проверка сохранения цены
    # Проверка обновления количества
    assert product1.quantity == product_dict_test[key_dict1]['quantity'] + product_dict_test[key_dict2]['quantity']


def test_create_product_new_product(product_dict_test):
    # Тестирование создания нового продукта
    key_dict1 = 'product1'
    key_dict2 = 'product4'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product.new_product(product_dict_test[key_dict2], [product1])
    assert isinstance(product2, Product)  # Ожидается, что новый продукт будет создан
    assert product2.name == product_dict_test[key_dict2]['name']  # Проверка имени
    assert product2.price == product_dict_test[key_dict2]['price']  # Проверка цены
    assert product2.quantity == product_dict_test[key_dict2]['quantity']  # Проверка количества


def test_price_setter_negative(capsys):
    # Создаем объект Product
    product = Product('name', 'description', 10.0, 10)

    # Устанавливаем некорректную цену
    product.price = -10.0

    # Захватываем вывод в консоль
    captured = capsys.readouterr()

    # Убираем лишние строки из captured.out
    relevant_output = "\n".join(
        line for line in captured.out.splitlines() if "Ошибка: Цена не должна быть" in line)

    # Проверяем только релевантное сообщение
    assert "Ошибка: Цена не должна быть нулевой или отрицательной." in relevant_output

    # Убеждаемся, что цена не изменилась
    assert product.price == 10.0


def test_price_setter_lower():
    # Проверка подтверждения понижения цены
    product = Product('name', 'description', 10.0, 10)
    with patch('builtins.input', return_value=''):
        product.price = 5.0  # Вводим меньшую цену без подтверждения
    # Проверяем, что цена не изменилась
    assert product.price == 10.0
    # Подтверждаем понижение цены
    with patch('builtins.input', return_value='y'):
        product.price = 5.0
    assert product.price == 5.0


def test_price_setter_raise():
    # Проверка увеличения цены
    product = Product('name', 'description', 10.0, 10)
    product.price = 15.0
    assert product.price == 15.0
