from src import App

from flask import Flask

from reactpy import component, html
from reactpy.backend.flask import configure


app = Flask(__name__)
configure(app, App)