import pytest
from app.controllers.report import ReportController


def test_get_most_request_ingredient(app, create_orders):
    get_most_requested_ingredient, _ = ReportController.get_most_requested_ingredient()
    pytest.assume(get_most_requested_ingredient['name'])
    pytest.assume(get_most_requested_ingredient['quantity'])


def test_get_most_valuable_clients(app, create_orders):
    get_most_valuable_clients, _ = ReportController.get_most_valuable_clients()
    for client in get_most_valuable_clients:
        pytest.assume(client['client_name'])


def test_get_month_with_most_revenue(app, create_orders):
    get_get_month_with_most_revenue, _ = ReportController.get_month_with_most_revenue()
    pytest.assume(get_get_month_with_most_revenue['month'])
    pytest.assume(get_get_month_with_most_revenue['total'])
