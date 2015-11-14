from flask import Blueprint, render_template

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    print 'todo: implement'
    return render_template('mod_main/landing_page/index.html')

@mod_main.route('/visu', methods=['GET'])
def visu():
    print 'todo: implement'
    return render_template('/visu/index.html')    
