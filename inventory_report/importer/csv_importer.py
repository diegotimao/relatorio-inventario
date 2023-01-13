import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".csv"):
            with open(path, "r", encoding="utf8") as arquivo:
                arquivo_csv = csv.DictReader(arquivo, delimiter=",")
                return [row for row in arquivo_csv]

        raise ValueError("Arquivo inválido")
