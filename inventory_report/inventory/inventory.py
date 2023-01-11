import csv
import json
from xml.dom import minidom
import os
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def get_file_csv(path):
        with open(path, "r", encoding="utf8") as arquivo:
            arquivo_csv = csv.DictReader(arquivo, delimiter=",")
            return [row for row in arquivo_csv]

    @staticmethod
    def get_file_json(path):
        with open(path) as file:
            file_list = json.load(file)
            return file_list

    @staticmethod
    def get_file_xml(path):
        with open(path, mode="r") as file:
            file_xml = minidom.parse(file)
            return file_xml

    @staticmethod
    def type_filename(path):
        arquivo, extensao = os.path.splitext(path)
        return extensao

    @staticmethod
    def import_data(path, type):
        extension = Inventory.type_filename(path)
        list = []

        if extension == ".csv":
            list = Inventory.get_file_csv(path)

        elif extension == ".json":
            list = Inventory.get_file_json(path)

        elif extension == ".xml":
            list = Inventory.get_file_xml(path)

        if type == "simples":
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)
