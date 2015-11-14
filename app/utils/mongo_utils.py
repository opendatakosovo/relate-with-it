class MongoUtils(object):
    mongo = None

    def __init__(self, mongo):
        self.mongo = mongo

    def save_currency(self, doc):
        self.mongo.db.currencies.save(doc)

    def save_project(self, doc):
       self.mongo.db.projects.save(doc)

    def get_currencies(self):
        cursor = self.mongo.db.currencies.find({})
        return list(cursor)

    def get_projects(self):
        cursor = self.mongo.db.projects.find({})
        return list(cursor)

    def get_expenses(self, region, dataset):
        cursor = self.mongo.db.dataset.find({
            'region.slug': region,
            'dataset.slug': dataset
        })

        return list(cursor)

    def insert_dataset_docs(self, doc):
        self.mongo.db.dataset.insert(doc)

    def remove_dataset_docs(self, region, dataset):
        self.mongo.db.dataset.remove({
            'region.name': region,
            'dataset.name': dataset
        })