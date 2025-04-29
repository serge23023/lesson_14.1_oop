import pytest

from classes.Product_Iterator import ProductIterator
from classes.product import Product

if __name__ == '__main__':  # pragma: no cover
    pytest.main()


def test_product_iterator(categories_test, product_dict_test):
    """
    Тестирование итератора `ProductIterator`.

    Args:
        categories_test (list[Category]): Список тестовых категорий.
        product_dict_test (dict): Тестовые данные продуктов.

    Assertions:
        - Проверка, что итератор корректно перебирает продукты в правильном порядке.
        - Проверка, что `StopIteration` вызывается после полного прохода по списку.
    """
    products = categories_test[0].products
    products.append(Product(**product_dict_test['product4']))  # Добавляем дополнительный товар для теста
    iterator = ProductIterator(products).__iter__()

    # Проверяем, что итератор возвращает продукты в правильном порядке
    for i in range(len(products)):
        assert next(iterator) == products[i]

    # Проверяем, что итератор генерирует исключение StopIteration после прохода по всем продуктам
    with pytest.raises(StopIteration):
        next(iterator)
