from reactpy import component, html


@component
def App():
    return html.div(
        {
            "style": {
                "textAlign": "center",
            }
        },
        html.header(
            {
                "style": {
                    "backgroundColor": "#282c34",
                    "minHeight": "100vh",
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "fontSize": "calc(10px + 2vmin)",
                    "color": "white",
                }
            },
            html.img({
                "src": "/public/logo.svg",
                "style": {
                    "height": "40vmin",
                    "pointerEvents": "none",
                }
            }),
            html.p(
                'Edit ',
                html.code('src/App.js'),
                ' and save to reload.'
            ),
            html.a(
                {
                    "className": "App-link",
                    "href": "https://reactpy.dev/docs/index.html",
                    "target": "_blank",
                    "rel": "noopener noreferrer",
                    "style": {
                        "color": "#61dafb"
                    }
                },
                'Learn ReactPy'
            )
        )
    )