#!/bin/bash

poetry init --name "{{ cookiecutter.app_name }}"
poetry add reactpy[flask] gunicorn