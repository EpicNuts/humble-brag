import pytest

from humble_brag.app import create_app

@pytest.yield_fixture(scope='session')
def app():
    """
    Setup the flask test app. This only gets executed once.

    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
        'WTF_CSRF_ENABLED': False
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    context = _app.app_context()
    context.push()

    yield _app

    context.pop()

@pytest.yield_fixture(scope='function')
def client(app):
    """
    Setup an app client. This gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()

