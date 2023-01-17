from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter


green_phrases_assertions = """\033[32mData de fabricação mais antiga:\033[0m \033[36m2020-09-06\033[0m
\033[32mData de validade mais próxima:\033[0m \033[36m2023-09-17\033[0m
\033[32mEmpresa com mais produtos:\033[0m \033[31mTarget Corporation\033[0m"""

# print("\033[36mAzul\033[0m \033[32mVerde\033[0m \033[31mVermelho\033[0m")


def test_decorar_relatorio():
    file = CsvImporter.import_data("inventory_report/data/inventory.csv")

    colored = ColoredReport(SimpleReport).generate(file)
    assert (colored) == green_phrases_assertions
