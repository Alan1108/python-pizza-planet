import pytest
import json


def test_get_index_service(client, index_uri):
    response = client.get(index_uri)
    pytest.assume(json.loads(response.data)['version'])
    pytest.assume(json.loads(response.data)['status'])
    pytest.assume(json.loads(response.data)['error'] == '')
