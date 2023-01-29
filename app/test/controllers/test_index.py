import pytest
from app.controllers import IndexController


def test_index_controller_test_connection(app):
    connection, error = IndexController.test_connection()
    pytest.assume(error == '')
    pytest.assume(connection)
