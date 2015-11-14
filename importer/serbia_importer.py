from abstract_importer import AbstractImporter
from slugify import slugify

class SerbiaImporter(AbstractImporter):

    def __init__(self):
        pass

    def get_csv_filename(self):
        return "importer/data/serbia/konsolidovani-rashodi-2010.csv"

    def get_region(self):
        return 'Serbia'

    def get_dataset(self):
        return 'Consolidated Expenses (2010)'

    def build_docs(self, row):

        # Clean expense string so that is is numerical (e.g. turn blank string to 0).
        cost = row[9].replace(',', '')
        if not cost.strip():
            cost = 0

        # Create doc.
        doc = {
            'region': {
                'name': self.get_region(),
                'slug': slugify(self.get_region(), to_lower=True),
                'subregion':{
                    'name': row[0],
                    'slug': slugify(row[0], to_lower=True),
                }
            },
            'activity':{
                'id': int(row[1]),
                'description': row[2]
            },
            'dataset': {
                'name': self.get_dataset(),
                'slug': slugify(self.get_dataset(), to_lower=True)
            },
            'cost': cost,
            'year': 2010
        }

        # Console output to provide user with feedback on status of importing process.
        print '%s - %s: %s (%s %i)' % (doc['activity']['id'], doc['activity']['description'], doc['cost'], doc['region']['name'], doc['year'])

        return [doc]