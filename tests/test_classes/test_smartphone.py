import pytest

if __name__ == '__main__':
    pytest.main()


def test_smartphone(smartphone_test):
    """
    Тестирование объекта `Smartphone`.

    Args:
        smartphone_test (Smartphone): Тестовый экземпляр класса `Smartphone`.

    Assertions:
        - Проверка уровня эффективности смартфона.
        - Проверка модели смартфона.
        - Проверка объёма памяти.
        - Проверка цвета устройства.
    """
    assert smartphone_test.efficiency == "Флагман"
    assert smartphone_test.model == "C23 Ultra"
    assert smartphone_test.memory == "256GB"
    assert smartphone_test.color == "Серый"
