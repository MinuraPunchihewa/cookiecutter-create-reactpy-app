from reactpy import component, html, run


@component
def App():
    return html.div(
        html.img({
            "src": "https://raw.githubusercontent.com/reactive-python/reactpy/main/branding/svg/reactpy-logo-square.svg"
        }),
        html.p('Edit src/App.py and save to reload.')
    )


run(App)