import pytest
from classes.Order_Classes.category import Category
from classes.Products_Classes.product import Product


if __name__ == '__main__':  # pragma: no cover
    pytest.main()


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


def test_add_product(categories_test, product_xiaomi, product_samsung):
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
