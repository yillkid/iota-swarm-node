curl http://localhost:8000 \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{"module":"tangleid", "command":"new_claim","uuid": "V9TCFLAOGGTAQATTJBLABAG9WY", "part_a":"V9TCFLAOGGTAQATTJBLABAG9WY","part_b":"V9TCFLAOGGTAQATTJBLABAGABB", "exp_date":"20191201", "claim_pic":"https://i.imgur.com/MxwIXXn.jpg", "msg":"TestingMessage"}'
