from dash.dependencies import Input, Output,State
#from data_loader import load_data
import plotly.express as px
import pyodbc
import pandas as pd
import plotly.graph_objects as go #Módulo para crear gráficos
import dash

def register_callbacks_layout0(app):
    @app.callback(
        [Output('url', 'pathname'), Output('error-messages', 'children')],
        Input('login-button', 'n_clicks'),
        [State('usuario', 'value'), State('password', 'value')]
    )
    def validate_login(n_clicks, usuario, password):
        if n_clicks:
            # Lógica de autenticación
            if usuario == "root" and password == "1234":
                # Si el login es exitoso, redirigir a la página principal
                return '/Principal', ""
            else:
                # Si falla, mostrar un mensaje de error
                return '/', "Usuario o contraseña incorrectos."


        

       
        
