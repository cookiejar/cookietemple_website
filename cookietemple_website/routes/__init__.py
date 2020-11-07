from flask import Blueprint

bp = Blueprint('basic', __name__)

from cookietemple_website.routes import routes  # noqa: E402, F401
