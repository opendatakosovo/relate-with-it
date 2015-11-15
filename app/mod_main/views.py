from flask import Blueprint, render_template, request
from app import mongo_utils
from app import lot_utils

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET'])
def index():
    projects = mongo_utils.get_projects()
    currencies = mongo_utils.get_currencies()
    return render_template('mod_main/index.html', projects=projects, currencies=currencies)

@mod_main.route('/visualizer/<project_slug>/<currency_slug>', methods=['GET'])
def visualizer(project_slug, currency_slug):

    format = request.args.get('format')
    if format != 'fit':

        project = mongo_utils.get_project(project_slug);
        currency = mongo_utils.get_currency(currency_slug);

        median_lot_size = lot_utils.get_median_lot_size(
            project['cost'],
            currency['kosovo']['value'],
            currency['montenegro']['value'],
            currency['serbia']['value'])

        total_lots_ks = lot_utils.get_total_lots(project['cost'], currency['kosovo']['value'], median_lot_size)
        total_lots_me = lot_utils.get_total_lots(project['cost'], currency['montenegro']['value'], median_lot_size)
        total_lots_sr = lot_utils.get_total_lots(project['cost'], currency['serbia']['value'], median_lot_size)

        lots = {
            'median': median_lot_size,
            'kosovo': total_lots_ks,
            'montenegro': total_lots_me,
            'serbia': total_lots_sr,
        }

        return render_template('/mod_main/visualizer.html',
                               project=project,
                               currency=currency,
                               lots=lots)

    else:
        return "Hey, it's the other format!"