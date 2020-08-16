from flask import Blueprint

bp = Blueprint('basic', __name__)

from cookietemple_website.basic import routes  # noqa: E402, F401
