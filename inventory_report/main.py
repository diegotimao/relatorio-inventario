from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def type_method(file_path):
    if file_path.endswith(".csv"):
        return CsvImporter

    if file_path.endswith(".json"):
        return JsonImporter

    if file_path.endswith(".xml"):
        return XmlImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    else:
        file_path = sys.argv[1]
        type = sys.argv[2]

        file = type_method(file_path)
        report = InventoryRefactor(file).import_data(file_path, type)

        print(report, end="")
