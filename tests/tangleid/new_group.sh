#!/bin/bash

source tests/common.sh

POST '{"extension":"tangleid","command":"new_group","group_name":"NCKU","group_picture":"https://s3-us-west-1.amazonaws.com/niusnews-imgs/146716_5.jpg","uuid":"ED9BCRDGJYWDHPTDNOPRULFWWG","pk":"SD9BCRDGJYWDHPTDNOPRULFWWG"}'
