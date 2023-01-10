import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def get_file_csv(path):
        with open(path, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.DictReader(arquivo, delimiter=",")
            return [row for row in arquivo_csv]

    @staticmethod
    def import_data(path, type):
        list = Inventory.get_file_csv(path)

        if type == "simples":
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)
