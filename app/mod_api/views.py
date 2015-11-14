from flask import Blueprint, Response
from app import mongo_utils
from bson import json_util

mod_api = Blueprint('api', __name__, url_prefix = '/api')

@mod_api.route('/', methods=['GET'])
def index():
    print 'todo: implement'
    return "Will be implemented soon! Come back tomorrow!"

@mod_api.route('/<region>/<dataset>', methods=['GET'])
def expenses(region, dataset):
    ''' Retrieve expenses based on region and dataset.

    :param region: slug representation of the region (e.g. kosovo)
    :param dataset: slug representation of the dataset (e.g. national-budget-execution)
    :return:
    '''
    results = mongo_utils.get_expenses(region, dataset)

    return Response(response=json_util.dumps(results),
                    status=200,
                    mimetype='application/json')