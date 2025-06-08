# Менеджер категорий и товаров

## 📑 Содержание

- [Описание](#-описание)
- [Структура классов](#-структура-классов)
  - [Category](#-category)
  - [Product](#-product)
  - [Smartphone](#-smartphone-наследник-product)
  - [LawnGrass](#-lawngrass-наследник-product)
  - [Order](#-order)
  - [MixinLogger](#-mixinlogger)
  - [Исключения](#-исключения)
- [Итератор](#-итератор)
- [Загрузка из JSON](#-загрузка-из-json)
- [Тестирование](#-тестирование)
- [Примеры](#-примеры)
- [Требования](#-требования)
- [Автор](#-автор)

---

## 🧠 Описание

Проект реализует объектно-ориентированную модель магазина с поддержкой:

- Категорий и продуктов
- Заказов
- Расширяемых товаров (смартфоны, газонная трава)
- Итерации по товарам
- Логирования объектов
- Загрузки из JSON
- Обработки ошибок и исключений
- Полного тестового покрытия

---

## 📚 Структура классов

### 🔹 `Category`
- Описывает категорию товаров
- Связана с одним или несколькими объектами `Product`
- Поддерживает счётчики созданных категорий и уникальных товаров
- Метод `middle_price()` возвращает среднюю цену всех товаров (0.0 при пустом списке)

### 🔹 `Product`
- Базовый класс товара
- Свойства: `name`, `description`, `price`, `quantity`
- Поддерживает сравнение (`__eq__`), сложение (`__add__`)
- Исключение при создании с `quantity=0`
- Цена защищена геттером/сеттером с валидацией и подтверждением понижения

### 🔹 `Smartphone` (наследник `Product`)
- Дополнительные поля: `efficiency`, `model`, `memory`, `color`

### 🔹 `LawnGrass` (наследник `Product`)
- Дополнительные поля: `country`, `germination_period`, `color`

### 🔹 `Order`
- Представляет заказ на товар
- Рассчитывает `total_cost = quantity × price`
- Обрабатывает `quantity <= 0` с сообщениями:
  - «Нельзя добавить товар с нулевым или отрицательным количеством.»
  - «Обработка оформления заказа завершена»

### 🔹 `MixinLogger`
- Миксин, логирующий создание объектов через `__repr__()`

### 🔹 Исключения
- `InvalidQuantityException` — вызывается при попытке добавить товар с `quantity <= 0` в категорию
- Используется в `Category` и `Order`
- Поддерживается `try / except / else / finally`

---

## 🔄 Итератор

### `ProductIterator`
Позволяет перебирать товары в категории:

```python
for product in ProductIterator(category.products):
    print(product)
```

---

## 📂 Загрузка из JSON

### `read_file.open_json()` + `utils.create_categories()`

```python
from utils import create_categories

categories = create_categories()
```

Пример `products.json`:

```json
[
  {
    "name": "Электроника",
    "description": "Смартфоны и устройства",
    "products": [
      {
        "name": "iPhone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }
    ]
  }
]
```

---

## 🧪 Тестирование

### 📦 Используются:
- `pytest`
- `pytest-cov`
- `fixtures` (`conftest.py`) для всех сущностей

### 🧪 Покрытие:
- Проверяются:
  - Исключения
  - Средняя цена в категории
  - Логика добавления товаров
  - Все пользовательские классы
- Запуск:
```bash
poetry run pytest --cov=src --cov-report=term-missing
```

---

## 🔍 Примеры

### ➕ Создание продукта
```python
product = Product("Телефон", "Модель X", 15000.0, 10)
```

### ❌ Ошибка при создании товара с нулевым количеством
```python
Product("Ошибка", "quantity = 0", 5000.0, 0)  # ValueError
```

### 🛒 Заказ
```python
order = Order(product, 3)
# Заказ: 3 × Телефон на сумму 45000.0 руб.
```

### 📦 Категория
```python
category = Category("Электроника", "Современные гаджеты")
category.add_product(product)
print(category.middle_price())  # средняя цена
```

---

## ✅ Требования
- Python 3.11+
- Poetry
- pytest
- pytest-cov

### Установка зависимостей:

```bash
poetry install
```

Все зависимости описаны в `pyproject.toml`.
