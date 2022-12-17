from typing import List, Dict
from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list: List[Dict]):
        data_atual = datetime.now()
        validade = []
        data_antiga = []
        companhia = []

        for item in list:
            data_antiga.append(item["data_de_fabricacao"])
            companhia.append(item["nome_da_empresa"])

            if (
                datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                >= data_atual
            ):
                validade.append(item["data_de_validade"])

        empresa = max(Counter(companhia))
        companhia_name = empresa.replace(" LIMITED", "")

        return (
            f"Data de fabricação mais antiga: {min(data_antiga)}\n"
            f"Data de validade mais próxima: {min(validade)}\n"
            f"Empresa com mais produtos: {companhia_name}"
        )
