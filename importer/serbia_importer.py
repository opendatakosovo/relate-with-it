from abstract_importer import AbstractImporter

class SerbiaImporter(AbstractImporter):

    def __init__(self):
        pass

    def get_csv_filename(self):
        return "data/serbia/xxx.csv"

    def get_region(self):
        return 'Serbia'

    def get_dataset(self):
        return 'xxx'

    def build_docs(row, self):
        pass