from src import App

from flask import Flask
from importlib import import_module


backend_module = import_module(f"reactpy.backend.{{cookiecutter.backend}}")
configure_function = getattr(backend_module, "configure")


app = Flask(__name__)
configure_function(app, App)