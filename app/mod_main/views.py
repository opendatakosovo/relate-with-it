from flask import Blueprint, render_template
from app import mongo_utils

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    projects = mongo_utils.get_projects()
    currencies = mongo_utils.get_currencies()
    return render_template('mod_main/index.html', projects=projects, currencies=currencies)

@mod_main.route('/visualizer/<project_id>/<currency_id>', methods=['GET'])
def visualizer(project_id, currency_id):
    project = mongo_utils.get_project(project_id);
    currency = mongo_utils.get_currency(currency_id);
    return render_template('/mod_main/visualizer.html', project=project, currency=currency)
