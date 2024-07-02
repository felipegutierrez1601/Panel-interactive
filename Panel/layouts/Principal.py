from dash import html, dcc
import plotly.express as px
from data_loader import load_data

def create_layout(app):
    df = load_data()
    
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    return html.Div(children=[
        html.H1(children='Ventana Principal'),

        dcc.Link('Recomendacion', href='/Recomendacion'),
        html.Br(),
        dcc.Link('Simulacion', href='/Simulacion'),
        html.Br(),
        dcc.Link('Refuerzo', href='/Refuerzo'),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])