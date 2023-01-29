import pytest
import json


def test_get_order_by_id_service(client, order_uri, create_orders):
    first_order = create_orders[0]
    currentOrder = json.loads(first_order.data)
    response = client.get(
        f'{order_uri}id/{currentOrder["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in currentOrder.items():
        pytest.assume(returned_order[0][param] == value)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {
        order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(json.loads(order.data)['_id'] in returned_orders)
