# IOTA Swarm Node

## Summary

`iota-swarm-node` is a proof-of-concept implementation of IOTA Swarm node, that
is a device with software/hardware implementing an algorithm aiming for
allowing several swarm nodes behave as a full node.

Most use cases for micropayments involve a single user or device interacting
repeatedly with a few vendors.

## Prerequisites
`iota-swarm-node`, writing with Python3+ compatible code as well as depending on [Pyota](https://github.com/iotaledger/iota.lib.py) is theoretically available for bot Python 3.5 and 3.6; yet, our testing result indicates that the environment for Python 3.6 is invalid in this case. Details as [Pyota issue#203](https://github.com/iotaledger/iota.lib.py/issues/203).

Install dependent packages:
```shell
$ sudo apt-get install python-pip python-setuptools python-dev python3-dev \
                       build-essential libssl-dev libffi-dev
```

Install official Python library for IOTA core:
```shell
$ pip install pyota
```

## Build from scratch

Ensure gcc or clang available in build environment and then execute:
```shell
$ make
```

(Optional) run test suite:
```shell
$ make check
```

## Launch the service

* Launch swarm node as server:

```shell
$ python server.py 
Listening on localhost:8000
```

* Generate an unused address:
```shell
$ python tests/generate_address.py
Generating an unused address ...
{u'addresses': [Address('OMAEMGRMASNBLYVFCRG9UARBBCWDIC9RGCOFTVAVJZDWISOHVMFLSW9ZL9FIJIHVVRYQLIMYBWEYP9WSX')]}
Duration: 73.5027749538 seconds
``` 

* Get tips from full node
```shell
$ python tests/get_tips.py
Getting tips ...
{u'duration': 484, u'branchTransaction': TransactionHash('QCPNKOXJXFERNNLTZZG9LBWDJQRLFIWDYNYQBHZJANJGXAADKNFTPWBWVDGHROVVVQWBKP9ROKRMZ9999'), u'trunkTransaction': TransactionHash('GEPJNFUNQGPDSFECJZGEWYYWYMGVWDCOELBKZQWILEUGGVHPNWFRLHNQHYKHCHPQWSQAXGYG9AIBA9999')}
Duration: 0.960033893585 seconds
``` 

* Send data (0 value transaction)
```shell
$ python tests/send_transfer.py
Send send transfer command ... 
WIAEHXJUVO9IDZXROJEDBQLFHVFLZCIQKPLLXCGWLNZFIUJZLBZACVLZPWAKUBYLDYRZKFIDKLSAHJHEY
Duration: 1.91658091545 seconds
```

## Licensing

`iota-swarm-node` is freely redistributable under the two-clause BSD License.
Use of this source code is governed by a BSD-style license that can be found
in the `LICENSE` file.
