from flask import Blueprint

mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET'])
def index():
	print 'todo: implement'