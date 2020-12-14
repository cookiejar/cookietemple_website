from flask import Flask
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)


from cookietemple_website.errors import bp as errors_bp  # noqa: E402

app.register_blueprint(errors_bp)

from cookietemple_website.routes import bp as basic_bp  # noqa: E402

app.register_blueprint(basic_bp)
