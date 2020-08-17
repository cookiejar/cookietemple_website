from cookietemple_website.errors import bp
from flask import render_template


@bp.app_errorhandler(400)
def bad_request_error(error):
    return render_template('errors/400.html'), 400


@bp.app_errorhandler(403)
def access_forbidden_error(error):
    return render_template('errors/403.html'), 403


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(410)
def unavailable_error(error):
    return render_template('errors/410.html'), 410


@bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
