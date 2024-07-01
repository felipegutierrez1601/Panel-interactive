from dash import html, dcc

def create_layout(app):
    return html.Div(children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])