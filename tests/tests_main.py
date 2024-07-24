from src.main import Category


def test_product_initialization(setup_data):
    """Проверяет корректность инициализации объектов Product"""
    data = setup_data
    assert data["product1"].name == "Samsung Galaxy S23 Ultra"
    assert data["product1"].description == "256GB, Серый цвет, 200MP камера"
    assert data["product1"].price == 180000.0
    assert data["product1"].quantity == 5

    assert data["product2"].name == "Iphone 15"
    assert data["product2"].description == "512GB, Gray space"
    assert data["product2"].price == 210000.0
    assert data["product2"].quantity == 8

    assert data["product3"].name == "Xiaomi Redmi Note 11"
    assert data["product3"].description == "1024GB, Синий"
    assert data["product3"].price == 31000.0
    assert data["product3"].quantity == 14


def test_category_initialization(setup_data):
    """Проверяет корректность инициализации объектов Category и подсчета количества категорий и продуктов"""
    data = setup_data

    assert data["category1"].name == "Смартфоны"
    assert (
        data["category1"].description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(data["category1"].products) == 3
    assert Category.category_count == 2  # Проверяем количество категорий
    assert Category.product_count == 4  # Проверяем общее количество товаров (в текущем тесте)

    assert data["category2"].name == "Телевизоры"
    assert (
        data["category2"].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(data["category2"].products) == 1


def test_product_count_update(setup_data):
    """Проверяет корректность обновления общего количества товаров"""
    data = setup_data

    # Количество товаров должно быть равно сумме товаров во всех категориях
    expected_product_count = len(data["category1"].products) + len(data["category2"].products)
    assert Category.product_count == expected_product_count
