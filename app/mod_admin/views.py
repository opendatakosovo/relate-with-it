from flask import Blueprint, render_template

mod_admin = Blueprint('admin', __name__, url_prefix = '/admin')

@mod_admin.route('/', methods=['GET'])
def index():
    return render_template('/mod_admin/index.html')


@mod_admin.route('/', methods=['GET', 'POST'])
def project():
    return render_template('/mod_admin/project.html')


@mod_admin.route('/', methods=['GET', 'POST'])
def unit():
    return render_template('/mod_admin/unit.html')