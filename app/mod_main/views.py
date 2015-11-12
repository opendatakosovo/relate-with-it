from flask import Blueprint, render_template

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    print 'todo: implement'
    return render_template('/landing/index.html')
