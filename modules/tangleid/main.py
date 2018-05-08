import time
import json
from swarm_node import get_tips, send_transfer

address = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"

def load(data):
    request_data = json.loads(data)
    
    if request_data['command'] == "new_claim":
        bundle_hash = new_claim(data)
        return bundle_hash
    elif request_data['command'] == "get_all_claims":
        list_claims = list_all_claims(data)
        return list_claims

def new_claim(data):
    ## Get tips
    dict_tips = get_tips(0)

    ## Set output transaction
    print ("Start to sransfer ... ")
    time_start_send = time.time()

    response = send_transfer("TEST", str(data), address, 0, dict_tips, debug=0)

    print "Response ... " + str(response)

    time_end = time.time()
    elapsed = time_end - time_start_send

    print "Duration: " + str(elapsed) + " seconds"

    return str(response)

def list_all_claims(data):
    return "Hello get all claims"
