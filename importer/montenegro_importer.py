from abstract_importer import AbstractImporter
from slugify import slugify

class MontenegroImporter(AbstractImporter):

    def __init__(self):
        pass

    def get_csv_filename(self):
        return "importer/data/montenegro/national-budget-execution-2011-2015.csv"

    def get_region(self):
        return 'Montenegro'

    def get_dataset(self):
        return 'National Budget Execution'

    def build_docs(self, row):

        # Each row can result in more than one document created...
        docs = []

        # In this case, it's because in the CSV doc there is a column for each year...
        years = [2011, 2012, 2013, 2014]

        # ... and we want a document for each year:
        for idx, year in enumerate(years):

            # Clean expense string so that is is numerical (e.g. turn blank string to 0).
            cost = row[2 + idx].replace(',', '')
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
                    'id': int(row[0]),
                    'description': row[1]
                },
                'cost': float(cost),
                'year': year
            }

            # Append to list of docs which will be returned for insertion.
            docs.append(doc)

            # Console output to provide user with feedback on status of importing process.
            print '%s - %s: %s (%s %i)' % (doc['activity']['id'], doc['activity']['description'], doc['cost'], doc['region']['name'], doc['year'])

        return docs
