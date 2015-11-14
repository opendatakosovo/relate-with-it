from abstract_importer import AbstractImporter

class KosovoImporter(AbstractImporter):

    def __init__(self):
        pass

    def get_csv_filename(self):
        return "data/kosovo/xxx.csv"

    def get_region(self):
        return 'Kosovo'

    def get_dataset(self):
        return 'xxx'

    def build_docs(row, self):
        pass