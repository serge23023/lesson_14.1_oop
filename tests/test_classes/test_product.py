from unittest.mock import patch
import pytest

from classes.Products_Classes.product import Product

if __name__ == '__main__':
    pytest.main()


def test_product(product_dict_test):
    """
    Тестирование создания объекта `Product` и проверки его атрибутов.

    Args:
        product_dict_test (dict): Тестовые данные продуктов.

    Assertions:
        - Проверка строкового представления объекта.
        - Проверка типа созданного объекта.
        - Проверка корректности имени, описания, цены и количества товара.
    """
    key_dict = 'product1'
    product1 = Product(**product_dict_test[key_dict])
    expected_repr = f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт."

    assert str(product1) == expected_repr
    assert isinstance(product1, Product)
    assert product1.name == product_dict_test[key_dict]['name']
    assert product1.description == product_dict_test[key_dict]['description']
    assert product1.price == product_dict_test[key_dict]['price']
    assert product1.quantity == product_dict_test[key_dict]['quantity']


def test_add_product(product_dict_test):
    """
    Тестирование сложения двух объектов `Product`.

    Args:
        product_dict_test (dict): Тестовые данные продуктов.

    Assertions:
        - Проверка корректности сложения стоимости двух объектов `Product`.
        - Проверка исключения `TypeError`, если объект не является `Product`.
    """
    key_dict1 = 'product2'
    key_dict2 = 'product3'
    product1 = Product(**product_dict_test[key_dict1])
    product2 = Product(**product_dict_test[key_dict2])

    assert product1 + product2 == 1100.0

    with pytest.raises(TypeError):
        product1 + "Not a product"


def test_price_setter_negative(capsys):
    """
    Тестирование проверки отрицательной цены.

    Args:
        capsys: Захват вывода в консоль.

    Assertions:
        - Проверка сообщения об ошибке при попытке установить отрицательную цену.
        - Проверка, что цена товара не изменилась.
    """
    product = Product('name', 'description', 10.0, 10)
    product.price = -10.0

    captured = capsys.readouterr()
    relevant_output = "\n".join(
        line for line in captured.out.splitlines() if "Ошибка: Цена не должна быть" in line
    )

    assert "Ошибка: Цена не должна быть нулевой или отрицательной." in relevant_output
    assert product.price == 10.0


def test_price_setter_lower():
    """
    Тестирование логики подтверждения понижения цены.

    Assertions:
        - Проверка, что цена не изменяется без подтверждения пользователя.
        - Проверка, что цена уменьшается при подтверждении пользователя.
    """
    product = Product('name', 'description', 10.0, 10)

    with patch('builtins.input', return_value=''):
        product.price = 5.0
    assert product.price == 10.0

    with patch('builtins.input', return_value='y'):
        product.price = 5.0
    assert product.price == 5.0


def test_price_setter_raise():
    """
    Тестирование увеличения цены.

    Assertions:
        - Проверка корректности увеличения цены.
    """
    product = Product('name', 'description', 10.0, 10)
    product.price = 15.0
    assert product.price == 15.0
