from __future__ import absolute_import

from flask import Blueprint
from experimental.api.v1 import API_V1_PREFIX

health_blueprint = Blueprint('health', __name__, url_prefix=API_V1_PREFIX)


@health_blueprint.route('/hello')
def hello():
    return "ok"
