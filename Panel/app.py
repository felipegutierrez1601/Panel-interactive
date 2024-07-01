from dash import Dash
from layouts import create_layout
from callbacks import register_callbacks

# Inicializar la aplicación Dash
app = Dash(__name__)

# Configurar el diseño de la aplicación (puedes elegir el layout que desees)
app.layout = create_layout(app)
# app.layout = layout2.create_layout(app)  # Descomenta esta línea para usar el segundo layout

# Configurar los callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True,port=8000)