#!/usr/bin/env python

"""Tests for `cookietemple_website` package."""
import pytest
from flask import Flask
from cookietemple_website.config import Config


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def create_test_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from cookietemple_website.errors import bp as errors_bp  # noqa: E402

    app.register_blueprint(errors_bp)

    from cookietemple_website.basic import bp as basic_bp

    app.register_blueprint(basic_bp)

    return app


def test_redirect():
    flask_app = create_test_app()

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
    response = testing_client.get('/')
    assert response.status_code == 302  # assert redirecting
