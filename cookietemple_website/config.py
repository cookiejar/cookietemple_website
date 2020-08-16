import os


class Config:
    CURRENT_DIR = os.path.abspath(os.getcwd())
    MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_PATH = os.path.join(MODULE_DIR, 'static')
    TEMPLATES_PATH = os.path.join(MODULE_DIR, 'templates')
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SOME_SUPERSECRETKEY'
