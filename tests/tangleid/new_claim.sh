#!/bin/bash

source common.sh

POST '{"extension":"tangleid", "command":"new_claim","uuid": "V9TCFLAOGGTAQATTJBLABAG9WY", "part_a":"V9TCFLAOGGTAQATTJBLABAG9WY","part_b":"V9TCFLAOGGTAQATTJBLABAGABB", "exp_date":"20191201", "claim_pic":"https://i.imgur.com/MxwIXXn.jpg", "msg":"TestingMessage"}'
