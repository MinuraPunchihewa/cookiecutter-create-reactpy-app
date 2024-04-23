from importlib import import_module


def get_app():
    backend = "{{cookiecutter.backend}}"

    if backend == "flask":
        from flask import Flask
        app = Flask(__name__)
    
    elif backend == "fastapi":
        from fastapi import FastAPI
        app = FastAPI()
    
    elif backend == "starlette":
        from starlette.applications import Starlette
        app = Starlette()

    else:
        raise ValueError(f"Invalid backend: {backend}")
    
    return app


def configure_app(app, App):
    reactpy_backend_module = import_module(f"reactpy.backend.{{cookiecutter.backend}}")
    configure_function = getattr(reactpy_backend_module, "configure")

    configure_function(app, App)



