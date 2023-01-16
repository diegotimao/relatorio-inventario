from inventory_report.inventory.product import Product

assertions = (
    "O produto farinha"
    " fabricado em 01-05-2021"
    " por Farinini com validade"
    " até 02-06-2023"
    " precisa ser armazenado ao abrigo de luz."
)


def test_relatorio_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "123456",
        "ao abrigo de luz",
    )

    assert str(product) == assertions
