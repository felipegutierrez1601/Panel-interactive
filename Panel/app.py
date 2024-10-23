from dash import Dash
from layouts import create_layout
from callbacks import register_callbacks
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


# Inicializar la aplicación Dash

class MyDashapp:
    def __init__(self):
        self.app = Dash(external_stylesheets=[dbc.themes.SOLAR])
        load_figure_template("SOLAR")
        

        # Configurar el diseño de la aplicación (puedes elegir el layout que desees)
        self.app.layout = create_layout(self.app)
        # app.layout = layout2.create_layout(app)  # Descomenta esta línea para usar el segundo layout

        # Configurar los callbacks
        register_callbacks(self.app)

    def run(self):
        self.app.run_server(debug=False,port=8000)

if __name__ == '__main__':
    aplicacion = MyDashapp()
    aplicacion.run()
