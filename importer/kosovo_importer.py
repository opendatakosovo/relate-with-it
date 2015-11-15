from abstract_importer import AbstractImporter
from slugify import slugify

class KosovoImporter(AbstractImporter):

    def __init__(self):
        pass

    def get_csv_filename(self):
        return "importer/data/kosovo/kosovo-budget-expenditures-2014.csv"

    def get_region(self):
        return 'Kosovo'

    def get_dataset(self):
        return 'Budget Expenditure (2014)'

    def build_docs(self, row):


        # In this case, it's because in the CSV doc there is a column for each year...
        year = row[3]

        # Clean expense string so that is is numerical (e.g. turn blank string to 0).
        cost = row[2].replace(',', '')
        if not cost.strip():
            cost = 0

        # Create doc.
        doc = {
            'region': {
                'name': self.get_region(),
                'slug': slugify(self.get_region(), to_lower=True)
            },
            'dataset': {
                'name': self.get_dataset(),
                'slug': slugify(self.get_dataset(), to_lower=True)
            },
            'activity': {
                'type': row[0],
                'description': row[1]
            },
            'cost': float(cost),
            'year': int(year)
        }


        # Console output to provide user with feedback on status of importing process.
        print '%s - %s: %s (%s %i)' % (doc['activity']['type'], doc['activity']['description'], doc['cost'], doc['region']['name'], doc['year'])

        return [doc]