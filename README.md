# IOTA Swarm Node

## Summary

iota-swarm-node is a proof-of-concept implementation of IOTA Swarm node, allowing
embedded devices to run their micro edition of full nodes distributed on more than
one device. That is, a swarm node is a device with software/hardware implementing
an algorithm aiming for allowing several swarm nodes behave as a full node.

Most use cases for micropayments involve a single user or device interacting
repeatedly with a few vendors.

## Prerequisites

Install dependent packages:
```shell
$ sudo apt-get install python-pip python-setuptools python-dev python3-dev build-essential libssl-dev libffi-dev
```

Install official Python library for IOTA Core:
```shell
$ pip install pyota
```

IOTA transaction PoW utilities:
```shell
$ git clone https://github.com/chenweiii/dcurl.git
$ cd dcurl
$ make check
$ cp ./libdcurl.so iota-swarm-node/
```

## Launch the service

* Swarm node (server side):
```shell
$ python server.py 
Listening on localhost:8000
```

* Generate a unused address:
```shell
$ python exanples/generate_address.py
Generating a unused address ... 
{u'addresses': [Address('OMAEMGRMASNBLYVFCRG9UARBBCWDIC9RGCOFTVAVJZDWISOHVMFLSW9ZL9FIJIHVVRYQLIMYBWEYP9WSX')]}
Duration: 73.5027749538 seconds
``` 

* Get tips from full node
```shell
$ python examples/get_tips.py
Getting tips ...
{u'duration': 484, u'branchTransaction': TransactionHash('QCPNKOXJXFERNNLTZZG9LBWDJQRLFIWDYNYQBHZJANJGXAADKNFTPWBWVDGHROVVVQWBKP9ROKRMZ9999'), u'trunkTransaction': TransactionHash('GEPJNFUNQGPDSFECJZGEWYYWYMGVWDCOELBKZQWILEUGGVHPNWFRLHNQHYKHCHPQWSQAXGYG9AIBA9999')}
Duration: 0.960033893585 seconds
``` 

* Send data (0 value transaction)
```shell
$ python examples/send_data.py
Send send transfer command ... 
WIAEHXJUVO9IDZXROJEDBQLFHVFLZCIQKPLLXCGWLNZFIUJZLBZACVLZPWAKUBYLDYRZKFIDKLSAHJHEY
Duration: 1.91658091545 seconds
```

## TODO
* Add [TangleID](https://github.com/TangleID/TangleID) module support.
