from reactpy import component, html


@component
def App():
    return html.div(
        html.img({
            "src": "/public/logo.svg"
        }),
        html.p('Edit src/App.py and save to reload.')
    )
