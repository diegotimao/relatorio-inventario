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

        companhia_names = Counter(companhia)
        list_products = ""

        for empresa in companhia_names:
            list_products += f"- {empresa}: {companhia_names[empresa]}\n"

        return (
            f"{simple}\n"
            f"Produtos estocados por empresa:\n"
            f"{list_products}"
        )
