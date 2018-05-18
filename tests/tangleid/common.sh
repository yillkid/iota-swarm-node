function POST {
    curl http://localhost:8000 \
        -X POST \
        -H 'Content-Type: application/json' \
        -d '$*'

    RES=$?
    if [ $RES -ne 0 ]; then
        echo 'Assert failed: "' $* '"'
        exit $RES
    fi
}
