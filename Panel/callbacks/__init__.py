from dash.dependencies import Input, Output, State
from layouts import  login_layout,Principal, Recomendacion, Refuerzo,Simulacion, Recomendacion_tablero,Refuerzo_tablero,Simulacion_tablero



import pandas as pd


def register_callbacks(app):
    """
    # Callback para mostrar el layout correcto según la URL
    @app.callback(
        Output('page-content_login', 'children'),
        Input('login-button', 'n_clicks'),
        State('url_login', 'pathname')
    )
    def display_page(n_clicks,pathname):
        if pathname == '/' or pathname == '/login':
            return create_login_layout()  # Mostrar layout de login
        elif pathname == '/Principal':
            
            return create_layout(app)  # Mostrar layout principal
        else:
            return '404 - Página no encontrada'

    # Callback para manejar el login
    @app.callback(
        [Output('url_login', 'pathname'), Output('error-messages', 'children')],
        Input('login-button', 'n_clicks'),
        [State('usuario', 'value'), State('password', 'value')]
    )
    def validate_login(n_clicks, usuario, password):
        if n_clicks:
            # Lógica de autenticación simple
            if usuario == "root" and password == "1234":
                # Redirigir al layout principal si el login es exitoso
                return '/Principal', ""
            else:
                # Mostrar mensaje de error si el login es incorrecto
                return '/malo', "Usuario o contraseña incorrectos."""

    @app.callback(
        Output('page-content', 'children'),
        [Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/Principal':
            return Principal.create_layout(app)
        elif pathname == '/Recomendacion':
            return Recomendacion.create_layout(app) 
        elif pathname == '/':
            return login_layout.create_login_layout(app)
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
    from .callbacks_loggin import register_callbacks_layout0

    from .callbacks_Recomendacion import register_callbacks_layout1
    from .callbacks_Simulacion import register_callbacks_layout2
    from .callbacks_Refuerzo import register_callbacks_layout3

    from .callbacks_Recomendacion_tablero import register_callbacks_layout4
    from .callbacks_Simulacion_tablero import register_callbacks_layout5
    from .callbacks_Refuerzo_tablero import register_callbacks_layout6


    register_callbacks_layout0(app)

    register_callbacks_layout1(app)
    register_callbacks_layout2(app)
    register_callbacks_layout3(app)

    register_callbacks_layout4(app)
    register_callbacks_layout5(app)
    register_callbacks_layout6(app)