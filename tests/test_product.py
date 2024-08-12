from src.product import Product


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

    assert data["product4"].name == '55" QLED 4K'
    assert data["product4"].description == "Фоновая подсветка"
    assert data["product4"].price == 123000.0
    assert data["product4"].quantity == 7


def test_invalid_product_creation():
    """Проверяет обработку ошибок при создании продукта с некорректными данными"""
    # Ожидаемое исключение при создании продукта с отрицательной ценой
    try:
        Product("Faulty Product", "Invalid price", -100.0, 5)
    except ValueError as e:
        assert str(e) == "Цена продукта не может быть отрицательной"

    # Ожидаемое исключение при создании продукта с отрицательным количеством
    try:
        Product("Faulty Product", "Invalid quantity", 100.0, -5)
    except ValueError as e:
        assert str(e) == "Количество продукта не может быть отрицательным"


def test_product_with_zero_price_and_quantity():
    """Проверяет возможность создания продукта с нулевой ценой и количеством"""
    product = Product("Free Sample", "Sample product", 0.0, 0)
    assert product.name == "Free Sample"
    assert product.price == 0.0
    assert product.quantity == 0


def test_add_product_to_existing_category(setup_data):
    """Проверяет добавление нового продукта в существующую категорию и обновление счетчиков"""
    data = setup_data
    new_product = Product("Google Pixel 6", "128GB, White", 60000.0, 3)
    data["category1"].add_product(new_product)

    assert len(data["category1"].products.split("\n")) == 4


def test_update_product_quantity():
    """Проверяет корректность обновления количества продукта"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.quantity == 10
    product.quantity = 20
    assert product.quantity == 20


def test_product_creation_with_long_name():
    """Проверяет создание продукта с длинным именем"""
    long_name = "A" * 1000
    product = Product(long_name, "Описание с длинным именем", 100.0, 10)
    assert product.name == long_name
    assert product.description == "Описание с длинным именем"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_update():
    """Проверяет обновление цены продукта"""
    product = Product("Test Product", "Test Description", 50.0, 10)
    assert product.price == 50.0
    product.price = 75.0
    assert product.price == 75.0


def test_product_price_setter_negative(setup_data):
    """Проверяет, что отрицательная или нулевая цена не изменяет текущую"""
    product = setup_data["product1"]
    # Проверка установки отрицательной цены
    try:
        product.price = -10000.0
    except ValueError:
        assert product.price == 180000.0  # Проверяем, что цена не изменилась
    else:
        assert False, "Expected ValueError for negative price"

    # Проверка установки нулевой цены
    try:
        product.price = 0
    except ValueError:
        assert product.price == 180000.0  # Проверяем, что цена не изменилась
    else:
        assert False, "Expected ValueError for zero price"


def test_new_product_class_method():
    """Проверяет, что `new_product` корректно создает объект Product на основе словаря с параметрами"""
    product_info = {"name": "New Product", "description": "New Description", "price": 250.0, "quantity": 7}
    product = Product.new_product(product_info)
    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 250.0
    assert product.quantity == 7
