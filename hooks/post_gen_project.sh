#!/bin/bash

# TODO: Add support for other backends: Sanic and Tornado
backend="{{ cookiecutter.backend }}"
server=""
run_command=""

if [ "$backend" == "flask" ]; then
    server="gunicorn"
    run_command="gunicorn main:app --reload"
elif [ "$backend" == "fastapi" ] || [ "$backend" == "starlette" ]; then
    server="uvicorn"
    run_command="uvicorn main:app --reload"
else 
    echo "Backend not supported!"
    exit 1
fi

echo "reactpy[$backend]" >> requirements.txt
echo "$server" >> requirements.txt

sed -i 's/<run_command>/'"$run_command"'/' README.md