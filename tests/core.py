import os
import json
import tempfile

import pytest

from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_generate_address(client):
    post_data = '{"command":"generate_address"}'
    rv = client.post('/', data=post_data)
    response = json.loads(rv.data)
    assert len(response['addresses']) > 0

    for address in response['addresses']:
        assert len(address) is 81

def test_get_tips_from_iri(client):
    TIPS_TYPE_IRI_REQULAR_ALGORITHM = 0
    post_data = {
        "command": "get_tips",
        "type": TIPS_TYPE_IRI_REQULAR_ALGORITHM,
    }
    rv = client.post('/', data=json.dumps(post_data))
    response = json.loads(rv.data)

    assert len(response['trunkTransaction']) is 81
    assert len(response['branchTransaction']) is 81

def test_get_tips_with_null(client):
    TIPS_TYPE_TWO_NULL_IOTA_TNX = 1
    post_data = {
        "command": "get_tips",
        "type": TIPS_TYPE_TWO_NULL_IOTA_TNX,
    }
    rv = client.post('/', data=json.dumps(post_data))
    response = json.loads(rv.data)

    assert len(response['trunkTransaction']) is 81
    assert len(response['branchTransaction']) is 81

def test_send_transfer(client):
    tag = "SWARMTEST"
    message = "TEST MESSAGE"
    address = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"
    value = 0
    TIPS_TYPE_TWO_NULL_IOTA_TNX = 1
    post_data = {
        'command': 'send_transfer',
        'tag': tag,
        'message': message,
        'address': address,
        'value': value,
        'tips_type': TIPS_TYPE_TWO_NULL_IOTA_TNX,
        'debug': 1
    }
    rv = client.post('/', data=json.dumps(post_data))
    assert len(rv.data) is 81
