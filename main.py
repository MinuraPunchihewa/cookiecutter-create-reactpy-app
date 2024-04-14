from reactpy import component, html
from reactpy.backend.flask import configure


@component
def App():
    return html.h1("Hello, world!")


app = Flask(__name__)
configure(app, HelloWorld)