from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, type):
        self.importer = type
        self.data = []

    def import_data(self, path, type):
        self.data += self.importer.import_data(path)

        if type == "simples":
            return SimpleReport.generate(self.data)
        else:
            return CompleteReport.generate(self.data)
