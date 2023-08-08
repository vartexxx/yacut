from http import HTTPStatus

from flask import jsonify, render_template

from . import app
from .models import URLMap
from .exceptions import InvalidAPIUsage


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    return render_template('core/404.html'), HTTPStatus.NOT_FOUND


def check_inique_short_url(custom_id):
    if URLMap.query.filter_by(short=custom_id).first():
        return custom_id
    return None
