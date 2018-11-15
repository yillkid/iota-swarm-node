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

def test_welcome_message(client):
    rv = client.get('/')
    assert b'Hello I am a swarm node.' in rv.data

def test_get_all_claims(client):
    post_data = '{"command":"get_all_claims","uuid": "V9TCFLAOGGTAQATTJBLABAG9WY"}'
    rv = client.post('/', data=post_data)
    assert len(json.loads(rv.data)) > 0

def test_get_all_notifies(client):
    post_data = '{"command":"get_all_notifies","uuid": "SD9BCRDGJYWDHPTDNOPRULFWWG"}'
    rv = client.post('/', data=post_data)
    assert len(json.loads(rv.data)) > 0

def test_get_all_revoke_claims(client):
    post_data = '{"command":"get_all_revoke_claims","uuid": "SD9BCRDGJYWDHPTDNOPRULFWWG"}'
    rv = client.post('/', data=post_data)
    print('rv.data' + str(rv.data))
    assert len(json.loads(rv.data)) > 0

def test_get_claim_info(client):
    post_data = '{"command":"get_claim_info","hash_txn": "UG9WOSTUUEXPTZSIWNLHIQSOAJAWFVGQWA9MBFSEQAIDNZLIVALAELPBAUNTCHRVYWYLONEFHESYSJ999"}'
    rv = client.post('/', data=post_data)
    assert type(json.loads(rv.data)) is dict

def test_login(client):
    post_data = '{"command":"login","uuid": "ED9BCRDGJYWDHPTDNOPRULFWWG"}'
    rv = client.post('/', data=post_data)
    assert len(json.loads(rv.data)) > 0

def test_new_claim(client):
    post_data = '{"extension":"tangleid", "command":"new_claim","uuid": "V9TCFLAOGGTAQATTJBLABAG9WY", "part_a":"V9TCFLAOGGTAQATTJBLABAG9WY","part_b":"V9TCFLAOGGTAQATTJBLABAGABB", "exp_date":"20191201", "claim_pic":"https://i.imgur.com/MxwIXXn.jpg", "msg":"TestingMessage"}'
    rv = client.post('/', data=post_data)
    assert len(rv.data) == 81

def test_new_group(client):
    post_data = '{"command":"new_group","first_name":"Huang", "cosignerp":"SD9BCRDGJYWDHPTDNOPRULFWWG","cosigners":"SD9BCRDGJYWDHPTDNOPRULFWWG", "last_name":"JyunYu","profile_picture":"https://s3-us-west-1.amazonaws.com/niusnews-imgs/146716_5.jpg", "uuid":"ED9BCRDGJYWDHPTDNOPRULFWWG","pk":"SD9BCRDGJYWDHPTDNOPRULFWWG"}'
    rv = client.post('/', data=post_data)
    print('rv.data' + str(rv.data))
    assert len(rv.data) == 81

def test_new_user(client):
    post_data = '{"command":"new_user","first_name":"Huang","cosignerp":"SD9BCRDGJYWDHPTDNOPRULFWWG","cosigners":"SD9BCRDGJYWDHPTDNOPRULFWWG","last_name":"JyunYu","profile_picture":"https://s3-us-west-1.amazonaws.com/niusnews-imgs/146716_5.jpg","uuid":"ED9BCRDGJYWDHPTDNOPRULFWWG","pk":"SD9BCRDGJYWDHPTDNOPRULFWWG"}'
    rv = client.post('/', data=post_data)
    assert len(rv.data) == 81

def test_revoke_claim(client):
    post_data = '{"command":"revoke_claim","uuid": "SD9BCRDGJYWDHPTDNOPRULFWWG","txnhash":"KQD9IKGNUM9ZVMHJHKVZLAAVDNDWJRNTZDYB9SXKMXPMBYNRGCOIMIVLTSRCJEXRAMWDNZODLBVR99999"}'
    rv = client.post('/', data=post_data)
    assert len(rv.data) == 81

def test_send_notify(client):
    post_data = '{"command":"send_notify","uuid":"SD9BCRDGJYWDHPTDNOPRULFWWG","receiver": "SD9BCRDGJYWDHPTDNOPRULFWWG","message":"HAPPYBIRTHDAY"}'
    rv = client.post('/', data=post_data)
    assert len(rv.data) == 81