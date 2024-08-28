from dash.dependencies import Input, Output
from layouts import Principal, Recomendacion, Refuerzo,Simulacion, Recomendacion_tablero,Refuerzo_tablero,Simulacion_tablero

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
        elif pathname == '/Recomendacion_tablero':
            return Recomendacion_tablero.create_layout(app)
        elif pathname == '/Refuerzo_tablero':
            return Refuerzo_tablero.create_layout(app)
        elif pathname == '/Simulacion_tablero':
            return Simulacion_tablero.create_layout(app)
        elif pathname == '/Simulacion':
            return Simulacion.create_layout(app)
    
    # Registrar callbacks específicos de cada layout
    from .callbacks_Recomendacion import register_callbacks_layout1
    from .callbacks_Simulacion import register_callbacks_layout2
    from .callbacks_Refuerzo import register_callbacks_layout3

    from .callbacks_Recomendacion_tablero import register_callbacks_layout4
    from .callbacks_Simulacion_tablero import register_callbacks_layout5
    from .callbacks_Refuerzo_tablero import register_callbacks_layout6


    register_callbacks_layout1(app)
    register_callbacks_layout2(app)
    register_callbacks_layout3(app)

    register_callbacks_layout4(app)
    register_callbacks_layout5(app)
    register_callbacks_layout6(app)