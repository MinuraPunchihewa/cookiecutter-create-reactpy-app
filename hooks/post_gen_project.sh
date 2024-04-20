#!/bin/bash

poetry init --name "{{ cookiecutter.app_name }}" --dependency "no" --dev-dependency "no"
poetry add reactpy[flask] gunicorn