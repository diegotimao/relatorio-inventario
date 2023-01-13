import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                file_list = json.load(file)
                return file_list

        raise ValueError("Arquivo inválido")
