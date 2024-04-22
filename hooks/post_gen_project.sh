#!/bin/bash

# TODO: Add support for other backends: Sanic and Tornado
backend="{{ cookiecutter.backend }}"
server=""

if [ "$backend" == "flask" ]; then
    server="gunicorn"
elif [ "$backend" == "fastapi" ] || [ "$backend" == "starlette" ]; then
    server="uvicorn"
else 
    echo "Backend not supported!"
    exit 1
fi

echo "reactpy[$backend]" >> requirements.txt
echo "$server" >> requirements.txt