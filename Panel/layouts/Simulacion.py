from dash import html, dcc
import plotly.express as px
from data_loader import load_data
"""
def create_layout(app):
    df = load_data()
    dcc.Interval(id = 'intervalo', interval = 1000)
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    return html.Div(children=[
        html.H1(children='Dashboard Simulacion'),

        dcc.Link('Recomendacion', href='/Recomendacion'),
        html.Br(),
        dcc.Link('Refuerzo', href='/Refuerzo'),

        dcc.Graph(
            id='Gra_simu',
            figure=fig
        )
    ])
"""