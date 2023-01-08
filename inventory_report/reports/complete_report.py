from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list: List[Dict]):
        simple = SimpleReport.generate(list)
        companhia = []

        for item in list:
            companhia.append(item["nome_da_empresa"])

        return f"{simple} " f"Produtos estocados por empresa:" f"- {companhia}"

        print(Counter(companhia))
