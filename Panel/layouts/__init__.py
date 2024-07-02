from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash import dcc ,ctx, dash_table
from dash import html


def create_layout(app):
    return html.Div(children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])