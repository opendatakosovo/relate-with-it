import abc
import csv
from app import mongo_utils

class AbstractImporter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_csv_filename(self): pass

    @abc.abstractmethod
    def get_region(self): pass

    @abc.abstractmethod
    def get_dataset(self): pass

    def execute(self):
        mongo_utils.remove_dataset_docs(self.get_region(), self.get_dataset())

        with open(self.get_csv_filename(), 'rb') as csvfile:
            reader = csv.reader(csvfile)

            # Skip the header
            next(reader, None)

            # Iterate through the rows, retrieve desired values.
            # Each row can result in more than one document created.
            for row in reader:
                docs = self.build_docs(row)
                mongo_utils.insert_dataset_docs(docs)

    @abc.abstractmethod
    def build_docs(self, row): pass


