from reactpy import component, html, run


@component
def App():
    return html.h1("Hello from ReactPy!")


run(App)