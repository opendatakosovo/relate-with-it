from flask import Blueprint, render_template
from app import mongo_utils

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    projects = mongo_utils.get_projects()
    currencies = mongo_utils.get_currencies()
    return render_template('mod_main/index.html', projects=projects, currencies=currencies)

@mod_main.route('/visualizer/<project_slug>/<currency_slug>', methods=['GET'])
def visualizer(project_slug, currency_slug):
    project = mongo_utils.get_project(project_slug);
    currency = mongo_utils.get_currency(currency_slug);
    return render_template('/mod_main/visualizer.html', project=project, currency=currency)
