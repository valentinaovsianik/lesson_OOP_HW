from src.product import Product


class Category:
    """Класс категории продуктов"""

    name: str
    description: str
    products: list[dict]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут для хранения продуктов
        Category.category_count += 1  # Увеличиваем счетчик категорий при создании нового объекта
        Category.product_count += sum(product.quantity for product in products)

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += product.quantity  # Увеличиваем общий счетчик на количество добавленного продукта
        else:
            raise TypeError("Можно добавлять только экземпляры класса Product или его наследников")

    @property
    def products(self):
        """Возвращает список продуктов в виде строки"""
        return "\n".join(str(product) for product in self.__products)

    def middle_price(self):
        """Подсчитывает средний ценник всех товаров в категории"""
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            middle_price = total_price / total_quantity
            return middle_price
        except ZeroDivisionError:
            print("На ноль делить нельзя.")
            return 0  # Возвращаем 0, если товаров нет и происходит деление на ноль
        except Exception as e:  # Обработка других возможных непредвиденных исключений
            print(f"Произошла ошибка: {e}")
            return 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
