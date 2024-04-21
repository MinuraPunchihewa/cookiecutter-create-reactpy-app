#!/bin/bash

# TODO: Add validation for the and Python version
# TODO: Add authors and licence
# TODO: Add support for other backends
poetry init \
    --name "{{ cookiecutter.app_name }}" \
    --description "{{ cookiecutter.description }}" \
    --python "{{ cookiecutter.python_version }}" \
    --dependency "reactpy[flask]" \
    --dependency "gunicorn" \
    --no-interaction
