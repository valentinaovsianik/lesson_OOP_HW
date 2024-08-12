from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, product_info):
        """Создает новый объект Product на основе словаря с параметрами"""
        pass
