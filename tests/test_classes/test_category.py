import pytest
from classes.Order_Classes.category import Category
from classes.Products_Classes.product import Product


def test_category_basics(categories_test):
    """Проверяет создание и базовые свойства категории."""
    category = categories_test

    assert isinstance(category, Category)
    assert category.name == 'Тестовая'
    assert category.description == 'Описание'
    assert isinstance(category.products, list)
    assert all(isinstance(p, Product) for p in category.products)

    # Категория должна содержать продукт из фикстуры
    assert len(category) == sum(p.quantity for p in category.products)
    assert str(category).startswith(f"\n{category.name}, количество продуктов:")
    assert Category.category_count >= 1  # type: ignore
    assert Category.product_count >= 1  # type: ignore


def test_add_product(categories_test, product_xiaomi, product_samsung, capsys):
    """Проверяет добавление и обновление товаров в категории."""
    category = categories_test
    initial_count: int = Category.product_count  # type: ignore

    # Добавляем новый продукт (уникальный name)
    product_new = Product(**product_xiaomi)
    category.add_product(product_new)
    assert Category.product_count == initial_count + 1
    assert any(p.name == product_new.name for p in category.products)

    # Добавляем дубликат (должен обновить, но не изменить count)
    category.add_product(product_new)
    assert Category.product_count == initial_count + 1

    # Добавляем ещё один уникальный
    another = Product(**product_samsung)
    category.add_product(another)
    assert Category.product_count == initial_count + 2

    # Некорректный тип
    with pytest.raises(TypeError):
        category.add_product("не продукт")  # type: ignore

    # Добавляем продукт с отрицательным или нулевым количеством
    another.quantity = -1
    category.add_product(another)
    captured = capsys.readouterr()
    assert "Нельзя добавить товар с нулевым или отрицательным количеством." in captured.out
    assert "Обработка добавления товара завершена" in captured.out


def test_middle_price_with_products():
    p1 = Product("Товар A", "desc", 100.0, 2)
    p2 = Product("Товар B", "desc", 200.0, 3)
    category = Category("Категория", "Описание", [p1, p2])
    assert category.middle_price() == 150.0


def test_middle_price_empty():
    category = Category("Пустая", "Нет товаров")
    assert category.middle_price() == 0.0

