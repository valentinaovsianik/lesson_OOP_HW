import pytest
from src.lawngrass import LawnGrass


def test_lawn_grass_addition():
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    # Ожидаемая сумма стоимости всей газонной травы
    expected_sum = (grass1.price * grass1.quantity) + (grass2.price * grass2.quantity)

    # Тестирование сложения двух объектов типа LawnGrass
    assert grass1 + grass2 == expected_sum
