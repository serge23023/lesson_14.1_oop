import pytest
from classes.Products_Classes.product import Product

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_product_basic_fields(product_iphone):
    """Проверка инициализации и полей объекта Product."""
    p = Product(**product_iphone)

    assert p.name == product_iphone["name"]
    assert p.description == product_iphone["description"]
    assert p.price == product_iphone["price"]
    assert p.quantity == product_iphone["quantity"]


def test_product_str(product_samsung):
    """Проверка __str__ метода."""
    p = Product(**product_samsung)
    expected = f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
    assert str(p) == expected


def test_product_repr(product_xiaomi):
    """Проверка __repr__ метода."""
    p = Product(**product_xiaomi)
    expected = f"Product('{p.name}', '{p.description}', {p.price}, {p.quantity})"
    assert repr(p) == expected


def test_product_addition(product_iphone, product_samsung):
    """Проверка сложения стоимости двух товаров."""
    p1 = Product(**product_iphone)
    p2 = Product(**product_samsung)
    total = p1 + p2
    expected = p1.price * p1.quantity + p2.price * p2.quantity
    assert total == expected


def test_product_addition_type_error(product_iphone):
    """Проверка ошибки при сложении с несовместимым типом."""
    p = Product(**product_iphone)
    with pytest.raises(TypeError):
        _ = p + "NotAProduct"  # type: ignore


def test_product_equality_true(product_iphone):
    """Проверка равенства двух одинаковых товаров."""
    p1 = Product(**product_iphone)
    p2 = Product(**product_iphone)
    assert p1 == p2


def test_product_equality_false(product_iphone, product_samsung):
    """Проверка неравенства разных товаров."""
    p1 = Product(**product_iphone)
    p2 = Product(**product_samsung)
    assert p1 != p2


def test_update_method(product_xiaomi):
    """Проверка метода update()."""
    p = Product(**product_xiaomi)
    p.update(999.0, 5)
    assert p.price == 999.0
    assert p.quantity == 14 + 5


def test_update_invalid_price(product_iphone):
    """Проверка ValueError при отрицательной цене в update()."""
    p = Product(**product_iphone)
    with pytest.raises(ValueError):
        p.update(0, 5)


def test_price_setter_raise():
    """Проверка повышения цены."""
    p = Product("test", "desc", 100.0, 1)
    p.price = 150.0
    assert p.price == 150.0


def test_price_setter_decline(monkeypatch):
    """Проверка отказа от понижения цены."""
    p = Product("test", "desc", 100.0, 1)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 50.0
    assert p.price == 100.0


def test_price_setter_confirm(monkeypatch):
    """Проверка подтверждённого понижения цены."""
    p = Product("test", "desc", 100.0, 1)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 50.0
    assert p.price == 50.0


def test_price_setter_negative_value(capsys):
    """Проверка ошибки при установке отрицательной цены."""
    p = Product("test", "desc", 100.0, 1)
    p.price = -10.0
    captured = capsys.readouterr()
    assert "Ошибка: Цена не должна быть нулевой или отрицательной." in captured.out
    assert p.price == 100.0
