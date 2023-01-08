from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list: List[Dict]):
        simple = SimpleReport.generate(list)
        companhia = []

        for item in list:
            companhia.append(item["nome_da_empresa"])
            print(companhia)
