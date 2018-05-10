import time
import json
from swarm_node import get_tips, send_transfer, \
    find_transactions_by_tag, get_txn_msg

address = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"

def load(data):
    request_data = json.loads(data)
    
    if request_data['command'] == "new_claim":
        bundle_hash = new_claim(data)
        return bundle_hash
    elif request_data['command'] == "get_all_claims":
        list_claims = list_all_claims(data)
        return list_claims
    elif request_data['command'] == "get_claim_info":
        result = get_claim_info(data)
        return result

def new_claim(data):
    data = json.loads(data)

    ## Get tips
    dict_tips = get_tips(0)

    ## Set output transaction
    print ("Start to sransfer ... ")
    time_start_send = time.time()

    tag = data['uuid'] + "C"
    response = send_transfer(tag, str(data), address, 0, dict_tips, debug=0)

    print "Response ... " + str(response)

    time_end = time.time()
    elapsed = time_end - time_start_send

    print "Duration: " + str(elapsed) + " seconds"

    return str(response)

def list_all_claims(data):
    data = json.loads(data)

    uuid = data['uuid']
    uuid = uuid + "C"

    #list_result = api.find_transactions(tags = [uuid])
    list_result = find_transactions_by_tag(uuid)

    return str(list_result)

def get_claim_info(data):
    data = json.loads(data)

    txn_hash = data['hash_txn']
    result = get_txn_msg(txn_hash)

    return result
