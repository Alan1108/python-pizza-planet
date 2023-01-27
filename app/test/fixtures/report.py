import pytest
from random import randint
from ..utils.functions import get_random_price, get_random_string


def ingredient_mock():
    return{
        'name': get_random_string(),
        'quantity': randint(10, 20)
    }


def month_mock():
    return{
        'month': get_random_string(),
        'total': get_random_price(150, 300)
    }


def clients_mock():
    return[{
        'client_name': get_random_string()
    }
        for _ in range(0, 3)
    ]


def report_mock() -> dict:
    return {
        'most_requested_ingredient': ingredient_mock(),
        'month_with_most_revenue': month_mock(),
        'most_valuable_clients': clients_mock()
    }


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def report():
    return report_mock()


@pytest.fixture
def get_report(client, report_uri, create_orders) -> dict:
    response = client.get(report_uri)
    return response
