import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".xml"):
            with open(path, mode="r", encoding="utf-8") as file:
                my_xml = file.read()
                file_xml = xmltodict.parse(my_xml)

                return file_xml["dataset"]["record"]
        raise ValueError("Arquivo inválido")
