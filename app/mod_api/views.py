from flask import Blueprint

mod_api = Blueprint('api', __name__, url_prefix = '/api')

@mod_api.route('/', methods=['GET'])
def index():
	print 'todo: implement'