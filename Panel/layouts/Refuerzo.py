from dash import html, dcc
import plotly.express as px
from data_loader import load_data

def create_layout(app):
    df = load_data()
    dcc.Interval(id = 'intervalo', interval = 1000)
    fig = px.line(df, x="Fruit", y="Amount", color="City")

    return html.Div(children=[
        html.H1(children='Dashboard  Refuerzo '),

        dcc.Link('Recomendacion', href='/Recomendacion'),
        html.Br(),
        dcc.Link('Simulacion', href='/Simulacion'),

        dcc.Graph(
            id='Grafico_refo',
            figure=fig
        )
    ])