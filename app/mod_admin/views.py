from flask import Blueprint, render_template, request
from currencyform import CurrencyForm
from projectform import ProjectForm

mod_admin = Blueprint('admin', __name__, url_prefix = '/admin')

@mod_admin.route('/', methods=['GET'])
def index():
    return render_template('/mod_admin/index.html')


@mod_admin.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'GET':
        return render_template('/mod_admin/project.html')
    else:
        form = ProjectForm(request)
        # TODO: persist in database using mongoutils.save()
        return render_template('/mod_admin/index.html')


@mod_admin.route('/currency', methods=['GET', 'POST'])
def currency():
    if request.method == 'GET':
        form = CurrencyForm()
        return render_template('/mod_admin/currency.html', form=form)

    else:
        form = CurrencyForm(request)
        # TODO: persist in database using mongoutils.save()
        return render_template('/mod_admin/index.html')