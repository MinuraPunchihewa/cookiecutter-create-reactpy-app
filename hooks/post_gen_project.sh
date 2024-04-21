#!/bin/bash

# TODO: Add validation for the app version and Python version
# TODO: Add authors and licence
poetry init \
    --name "{{ cookiecutter.app_name }}" \
    --description "{{ cookiecutter.description }}" \
    --version "{{ cookiecutter.version }}" \
    --python "{{ cookiecutter.python_version }}" \
    --dependency "reactpy[flask]" \
    --dependency "gunicorn" \
    --no-interaction