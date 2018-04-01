from __future__ import absolute_import

from flask import Blueprint, request

from experimental.api.v1 import API_V1_PREFIX
from experimental.model.demo import DemoModel

demo_blueprint = Blueprint('demo', __name__, url_prefix=API_V1_PREFIX)


@demo_blueprint.route('/demo', methods=['GET', 'POST'])
def demo():
    if request.method == 'GET':
        return DemoModel.get_by_name(request.args['name'])
    else:
        return DemoModel.new(request.args['name'])
