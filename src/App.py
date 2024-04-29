from reactpy import component, html
from src.styles import App as App_, App_logo, App_header, App_link, body, code


@component
def App():
    return html.div(
        {
            "style": App_.update(body)
        },
        html.header(
            {
                "style": App_header
            },
            html.img({
                "src": "/public/logo.svg",
                "style": App_logo
            }),
            html.p(
                'Edit ',
                html.code(
                    {
                        "style": code
                    },
                    'src/App.js'
                ),
                ' and save to reload.'
            ),
            html.a(
                {
                    "className": "App-link",
                    "href": "https://reactpy.dev/docs/index.html",
                    "target": "_blank",
                    "rel": "noopener noreferrer",
                    "style": App_link
                },
                'Learn ReactPy'
            )
        )
    )