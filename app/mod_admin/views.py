from flask import Blueprint, render_template, request, url_for, redirect
from currencyform import CurrencyForm
from projectform import ProjectForm
from app import mongo_utils

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')

@mod_admin.route('/', methods=['GET'])
def index():
    currencies = mongo_utils.get_currencies()
    projects = mongo_utils.get_projects()
    return render_template('/mod_admin/index.html', projects=projects, currencies=currencies)


@mod_admin.route('/project', methods=['GET', 'POST'])
def project():
    if request.method == 'GET':
        form = ProjectForm()
        return render_template('/mod_admin/project.html', form=form)

    else:
        form = ProjectForm(request.form)
        doc = {
            'region': form.region.data,
            'name': form.name.data,
            'description': form.description.data,
            'cost': float(form.cost.data),
            'currency': form.currency.data,
            'source': {
                'type': form.source_type.data,
                'reference': form.source_ref.data
            },
            'imageUrl': form.image_url.data
        }
        mongo_utils.save_project(doc)

        return redirect(url_for('admin.index'))


@mod_admin.route('/currency', methods=['GET', 'POST'])
def currency():
    if request.method == 'GET':
        form = CurrencyForm()
        return render_template('/mod_admin/currency.html', form=form)

    else:
        form = CurrencyForm(request.form)
        doc = {
            'name': form.name.data,
            'description': form.description.data,
            'kosovo': {
                'value': float(form.value_ks.data),
                'source': form.source_ks.data
            },
            'montenegro': {
                'value': float(form.value_me.data),
                'source': form.source_me.data
            },
            'serbia': {
                'value': float(form.value_rs.data),
                'source': form.source_rs.data
            },
            'imageUrl': form.image_url.data
        }
        mongo_utils.save_currency(doc)

        return redirect(url_for('admin.index'))
