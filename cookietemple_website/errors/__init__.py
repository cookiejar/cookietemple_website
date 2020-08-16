from flask import Blueprint

bp = Blueprint('errors', __name__)

from cookietemple_website.errors import handlers  # noqa: E402, F401
