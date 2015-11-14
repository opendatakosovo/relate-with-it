from flask import Blueprint, render_template
from app import mongo_utils

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    projects = mongo_utils.get_projects()
    currencies = mongo_utils.get_currencies()
    return render_template('mod_main/landing_page/index.html', projects=projects, currencies=currencies)

@mod_main.route('/visu', methods=['GET'])
def visu():
    print 'todo: implement'
    return render_template('/visu/index.html')    
