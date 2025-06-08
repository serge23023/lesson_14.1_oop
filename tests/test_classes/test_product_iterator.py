import pytest

from classes.Products_Classes.product_iterator import ProductIterator
from classes.Products_Classes.product import Product


if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_product_iterator(categories_test, product_xiaomi):
    """
    Тестирование итератора `ProductIterator`.

    Args:
        categories_test (Category): Категория с товарами.
        product_xiaomi (dict): Дополнительный товар.

    Assertions:
        - Проверка корректного порядка итерации.
        - Проверка генерации StopIteration после завершения.
    """
    products = categories_test.products
    products.append(Product(**product_xiaomi))  # добавляем второй товар

    iterator = iter(ProductIterator(products))

    for i in range(len(products)):
        assert next(iterator) == products[i]

    with pytest.raises(StopIteration):
        next(iterator)
