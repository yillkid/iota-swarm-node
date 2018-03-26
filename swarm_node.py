# -*- coding: utf-8 -*-
import subprocess
import tempfile

import iota
from iota import Iota, Address
from iota.crypto.signing import SignatureFragmentGenerator
from iota.crypto.kerl.conv import convertToBytes, convertToTrits, \
  trits_to_trytes, trytes_to_trits

from config import SEED

TXN_SECURITY_LEVEL = 2
DEPTH = 7

api = Iota('http://node.deviceproof.org:14265', seed = SEED)
# api = Iota('http://cryptoiota.win:14265', seed = SEED)

def insert_to_trytes(index_start, index_end, str_insert, trytes):
    trytes = trytes[:index_start] + str_insert + trytes[index_end:]

    return trytes

# Return a unused IOTA address
def gen_a_address():
    print "Generating a unused address ..."
    return api.get_new_addresses(count = None, index = None)

# Get transaction tips
# Parameter:
# 0: Request getTransactionToApprove RestfulAPI to fullnode
# 1: Return two null transaction
# 2: Get tips list from fullnode
def get_tips(tips_type):
    if tips_type == 0:
        return api.get_transactions_to_approve(DEPTH)
    if tips_type == 1:
        return {'trunkTransaction':iota.Hash(''), 'branchTransaction':iota.Hash('')}
    if tips_type == 2:
	return api.get_tips()

def send_transfer(tag, message, address, values, dict_tips):
    ## Set output transaction
    print ("Start to sransfer ... ")

    propose_bundle = iota.ProposedBundle()

    print ("Setting output transaction ...")
    txn_output = iota.ProposedTransaction(
         address = iota.Address(address),
         value = values,
         tag = iota.Tag(tag),
         message = iota.TryteString(message)
    )

    propose_bundle.add_transaction(txn_output)

    # Get input address
    if int(values) > 0:
        print "DEBUG values = " + str(values)

        print "Checking input balance ..."
        dict_inputs = api.get_inputs()
        if int(dict_inputs['totalBalance']) < int(values):
            print "Balance not enough"
            return 0

    ## Setting intput transaction
    if int(values) > 0:
        print ("Setting input transaction ...")
        value_input = 0
        index_input = 0
        while (int(value_input) < int(values)):
            addy = iota.Address(dict_inputs['inputs'][index_input])
            addy.balance = dict_inputs['inputs'][index_input].balance
            addy.key_index = 1
            addy.security_level = TXN_SECURITY_LEVEL

            propose_bundle.add_inputs([addy])
            value_input = value_input + int(dict_inputs['inputs'][0].balance)

        # Send unspent inputs to
        print ("Setting unspent input to a new address ...")
        unspent = iota.Address(gen_a_address()['addresses'][0])
        propose_bundle.send_unspent_inputs_to(unspent)

    # This will get the bundle hash
    print ("Bundle finalize ...")
    propose_bundle.finalize()

    ## Signing
    # If the transaction need sign, it will then sign-up the transaction
    # to fill up signature fragements
    if int(values) > 0:
        print ("Signing...")
        propose_bundle.sign_inputs(iota.crypto.signing.KeyGenerator(SEED))

    trytes = propose_bundle.as_tryte_strings()

    ## Get tips by getTransactionsToApprove
    trunk_hash = dict_tips['branchTransaction']
    branch_hash = dict_tips['trunkTransaction']

    # Do PoW (attach to tangle)
    for tx_tryte in trytes:
        # TODO: Timestamp
        # timestamp = None
        # timestamp_lower_bound = None
        # timestamp_upper_bound = None

        # Tips insert - trunk
        tx_tryte = insert_to_trytes(2430, 2511, str(trunk_hash), tx_tryte) 
        # Tips insert - branch 
        tx_tryte = insert_to_trytes(2511, 2592, str(branch_hash), tx_tryte) 

        # Do PoW for this transaction
        print "Do POW for this transaction ..."
        nonce = ''
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(['python', 'tx_search_nonce.py', str(tx_tryte)], stdout=tempf)
            proc.wait()
            tempf.seek(0)
            nonce = tempf.read().rstrip()

            tx_tryte = insert_to_trytes(2646, 2673, str(nonce), tx_tryte) 

            print "Prepare to broadcast ..."

	    try:
   	        api.broadcast_transactions([tx_tryte[0:2673]])
            except Exception as e:
                print "Error: " + str(e.context)

    return propose_bundle.hash

tag = "YILLKID"
message = "HELLO"
address = "BXEOYAONFPBGKEUQZDUZZZODHWJDWHEOYY9AENYF9VNLXZHXBOODCOTYXW9MGGINTEJPLK9AGOPTPODVX"
value = 1

# Get tips
#dict_tips = get_tips(0)

#print send_transfer(tag, message, address, value, dict_tips)
