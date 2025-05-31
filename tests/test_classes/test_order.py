import pytest
from classes.Order_Classes.order import Order
from classes.Products_Classes.product import Product


if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_order_creation(product_iphone):
    """Проверка создания объекта Order и вычисления total_cost."""
    product = Product(**product_iphone)
    order = Order(product, 3)

    assert isinstance(order, Order)
    assert order.product == product
    assert order.quantity == 3
    assert order.total_cost == 3 * product.price


def test_order_str(product_iphone):
    """Проверка строкового представления заказа."""
    product = Product(**product_iphone)
    order = Order(product, 2)

    expected = f"Заказ: 2 × {product.name} на сумму {2 * product.price} руб."
    assert str(order) == expected


def test_order_repr(product_iphone):
    """Проверка технического представления заказа."""
    product = Product(**product_iphone)
    order = Order(product, 1)

    expected = f"Order('{product.name}', 1, {product.price})"
    assert repr(order) == expected


def test_order_negative_quantity(product_iphone):
    """Проверка ошибки при создании заказа с отрицательным количеством."""
    product = Product(**product_iphone)

    with pytest.raises(ValueError):
        Order(product, 0)
