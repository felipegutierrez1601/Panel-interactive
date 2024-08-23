from dash.dependencies import Input, Output
from layouts import Principal, Recomendacion, Refuerzo,Simulacion

import pandas as pd


def register_callbacks(app):
    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/Principal':
            return Principal.create_layout(app)
        elif pathname == '/Recomendacion':
            return Recomendacion.create_layout(app)
        elif pathname == '/Refuerzo':
            return Refuerzo.create_layout(app)
        else:
            return Simulacion.create_layout(app)
    
    # Registrar callbacks específicos de cada layout
    from .callbacks_Recomendacion import register_callbacks_layout1
    from .callbacks_Simulacion import register_callbacks_layout2
    from .callbacks_Refuerzo import register_callbacks_layout3

    register_callbacks_layout1(app)
    register_callbacks_layout2(app)
    register_callbacks_layout3(app)