from src.main import Category, Product


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


def test_category_initialization(setup_data):
    """Проверяет корректность инициализации объекта Category"""
    category = setup_data["category1"]
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_product_count_update(new_setup_data):
    """Проверяет корректность обновления общего количества товаров"""
    data = new_setup_data

    # Получаем список всех продуктов в категориях
    products_in_category1 = data["category1"]._Category__products
    products_in_category2 = data["category2"]._Category__products

    # Подсчитываем общее количество товаров в каждой категории
    total_quantity = sum(product.quantity for product in products_in_category1) + sum(
        product.quantity for product in products_in_category2
    )

    # Проверяем, что общее количество продуктов совпадает с фактическим значением
    assert total_quantity == Category.product_count


def test_additional_product_and_category():
    """Проверяет увеличение количества товаров и категорий при добавлении новых объектов"""
    Category.category_count = 0  # Сброс счетчиков

    # Создаем дополнительные продукты и категории
    product5 = Product("Huawei P50 Pro", "256GB, Черный", 100000.0, 10)
    product6 = Product("Sony Xperia 1", "128GB, Белый", 80000.0, 6)
    category3 = Category("Новые Смартфоны", "Последние модели смартфонов", [product5, product6])

    assert Category.category_count == 1
    assert len(category3.products.split("\n")) == 2


def test_empty_category():
    """Проверяет корректность создания категории без продуктов"""
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создаем категорию без продуктов
    empty_category = Category("Пустая Категория", "Категория без продуктов", [])

    assert empty_category.name == "Пустая Категория"
    assert empty_category.description == "Категория без продуктов"
    assert len(empty_category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


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


def test_category_without_description():
    """Проверяет возможность создания категории без описания"""
    category = Category("No Description", "", [])
    assert category.name == "No Description"
    assert category.description == ""
    assert len(category.products) == 0


def test_add_product_to_existing_category(setup_data):
    """Проверяет добавление нового продукта в существующую категорию и обновление счетчиков"""
    data = setup_data
    new_product = Product("Google Pixel 6", "128GB, White", 60000.0, 3)
    data["category1"].add_product(new_product)

    assert len(data["category1"].products.split("\n")) == 4


def test_create_empty_product_list_category():
    """Проверяет возможность создания категории с пустым списком продуктов"""
    empty_product_list_category = Category("Empty Product List", "Категория без продуктов", [])
    assert empty_product_list_category.name == "Empty Product List"
    assert empty_product_list_category.description == "Категория без продуктов"
    assert len(empty_product_list_category.products) == 0


def test_update_product_quantity():
    """Проверяет корректность обновления количества продукта"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.quantity == 10
    product.quantity = 20
    assert product.quantity == 20


def test_reset_category_and_product_counts():
    """Проверяет сброс счетчиков категорий и продуктов"""
    Category.category_count = 10
    Category.product_count = 50

    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0


def test_category_description_update():
    """Проверяет обновление описания категории"""
    category = Category("Test Category", "Initial Description", [])
    category.description = "Updated Description"

    assert category.description == "Updated Description"


def test_category_with_large_number_of_products():
    """Проверяет создание категории с большим количеством продуктов"""
    products = [Product(f"Product {i}", "Description", 10.0, 1) for i in range(1000)]
    category = Category("Large Category", "Категория с большим количеством продуктов", products)

    assert category.name == "Large Category"
    assert len(category.products.split("\n")) == 1000


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
    product.price = -10000.0
    assert product.price == 180000.0
    product.price = 0
    assert product.price == 180000.0


def test_new_product_class_method():
    """Проверяет, что `new_product` корректно создает объект Product на основе словаря с параметрами"""
    product_info = {"name": "New Product", "description": "New Description", "price": 250.0, "quantity": 7}
    product = Product.new_product(product_info)
    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 250.0
    assert product.quantity == 7
