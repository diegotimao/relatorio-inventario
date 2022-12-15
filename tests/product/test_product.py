from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = "Api Backend"
    nome_da_empresa = "Dev Programar"
    data_de_fabricacao = "11-02-1999"
    data_de_validade = "02-02-2022"
    numero_de_serie = "007"
    instrucoes_de_armazenamento = "Banco dados"

    is_product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert is_product.id == 1
    assert is_product.nome_do_produto == "Api Backend"
    assert is_product.nome_da_empresa == "Dev Programar"
    assert is_product.data_de_fabricacao == "11-02-1999"
    assert is_product.data_de_validade == "02-02-2022"
    assert is_product.numero_de_serie == "007"
    assert is_product.instrucoes_de_armazenamento == "Banco dados"
