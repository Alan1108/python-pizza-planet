import pytest
from flask import jsonify


def test_report_service(report):
    pytest.assume(report['most_requested_ingredient'])
    pytest.assume(report['month_with_most_revenue'])
    pytest.assume(report['most_valuable_clients'])


def test_get_report_service(client, create_orders, report, report_uri):
    response = client.get(report_uri).json
    returned_report = {
        "most_requested_ingredient": response['most_requested_ingredient'],
        "month_with_most_revenue": response['month_with_most_revenue'],
        "most_valuable_clients": response['most_valuable_clients']
    }
    pytest.assume(returned_report['most_requested_ingredient'])
    pytest.assume(returned_report['month_with_most_revenue'])
    pytest.assume(returned_report['most_valuable_clients'])
