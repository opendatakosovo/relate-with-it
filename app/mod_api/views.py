from flask import Blueprint, Response
from app import mongo_utils
from bson import json_util

mod_api = Blueprint('api', __name__, url_prefix = '/api')

@mod_api.route('/', methods=['GET'])
def index():
    print 'todo: implement'
    return "Will be implemented soon! Come back tomorrow!"


@mod_api.route('/dataset/<region>/<dataset>', methods=['GET'])
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


@mod_api.route('/projects', methods=['GET'])
def projects():
    results = mongo_utils.get_projects()
    return Response(response=json_util.dumps(results),
                    status=200,
                    mimetype='application/json')


@mod_api.route('/currencies', methods=['GET'])
def currencies():
    results = mongo_utils.get_currencies()
    return Response(response=json_util.dumps(results),
                    status=200,
                    mimetype='application/json')


@mod_api.route('/projects/delete/<id>', methods=['POST'])
def remove_project(id):
    mongo_utils.remove_project(id)
    return Response(status=200)


@mod_api.route('/currencies/delete/<id>', methods=['POST'])
def remove_currency(id):
    mongo_utils.remove_currency(id)
    return Response(status=200)