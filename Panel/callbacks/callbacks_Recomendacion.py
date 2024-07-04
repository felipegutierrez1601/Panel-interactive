from dash.dependencies import Input, Output,State
from data_loader import load_data
import plotly.express as px

def register_callbacks_layout1(app):
    @app.callback(
    [Output('link-1', 'style'),
     Output('link-2', 'style'),
     Output('link-3', 'style')],
    [Input('navegador', 'pathname')]
    )

    def update_link_styles(pathname):
        # Estilos base para los enlaces
        base_style = {'fontSize': '20px', 'padding': '10px', 'textDecoration': 'none', 'color': 'black', 'margin': '0 20px'}
        selected_style = {'fontSize': '30px', 'padding': '10px', 'textDecoration': 'none', 'color': 'blue', 'margin': '0 20px'}
        
        link1_style = base_style
        link2_style = base_style
        link3_style = base_style

        # Update the selected link style
        if pathname == '/page-1':
            link1_style = selected_style
        elif pathname == '/page-2':
            link2_style = selected_style
        elif pathname == '/page-3':
            link3_style = selected_style

        return link1_style, link2_style, link3_style
