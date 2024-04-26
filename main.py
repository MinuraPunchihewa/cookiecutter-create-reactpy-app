from src import App

from flask import Flask
from reactpy.backend.flask import configure


app = Flask(__name__, static_folder="public")
configure(app, App)