#!/bin/bash

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

# TODO: Add validation for the and Python version
# TODO: Add authors and licence
# TODO: Add support for other backends: Sanic and Tornado
poetry init \
    --name "{{ cookiecutter.app_name }}" \
    --description "{{ cookiecutter.description }}" \
    --python "{{ cookiecutter.python_version }}" \
    --dependency "reactpy[${backend}]" \
    --dependency "${server}" \
    --no-interaction
