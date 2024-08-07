from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный базовый класс продуктов"""

    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления продукта"""
        pass


    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод для сложения продуктов"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_info):
        """Создает новый объект Product на основе словаря с параметрами"""
        pass
