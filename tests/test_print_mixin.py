from src.product import Product


def test_print_mixin(capsys):
    """Тестирует вывод информации о продукте"""
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    captured_before = capsys.readouterr()
    print(repr(product))
    captured_after = capsys.readouterr()
    expected_output = 'Product(55" QLED 4K, Фоновая подсветка, 123000.0, 7)'
    assert expected_output in captured_before.out.strip()
    assert captured_after.out.strip() == expected_output
