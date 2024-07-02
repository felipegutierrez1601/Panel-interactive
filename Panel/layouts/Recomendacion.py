from dash import html, dcc, dash_table
import plotly.express as px
from data_loader import load_data
import dash_daq as daq
import dash_bootstrap_components as dbc
from utils import widget_fecha


"""def create_layout(app):
    df = load_data()
    dcc.Interval(id = 'intervalo', interval = 1000)
    fig = px.line(df, x="Fruit", y="Amount", color="City")

    return html.Div(children=[
        html.H1(children='Dashboard  Recomendacion '),

        dcc.Link('Principal', href='/Principal'),
        html.Br(),
        dcc.Link('Simulacion', href='/Simulacion'),
        html.Br(),
        dcc.Link('Refuerzo', href='/Refuerzo'),

        dcc.Graph(
            id='Grafico_reco',
            figure=fig
        )
    ])"""


def create_layout(app):
    recomendacion =html.Div([

        dbc.Card(html.Div(
            ), className = "recomendacion_card_1"),
        dbc.Card(html.Div(
            ), className = "recomendacion_card_2"),
        dbc.Card(html.Div(
            ), className = "recomendacion_card_3"),
        dbc.Card(html.Div(
            ), className = "recomendacion_card_4"),
        dbc.Card(html.Div(
            ), className = "recomendacion_card_5"),
        html.Div(className="Logo_UBB"),
        html.Div(className="Logo_Arauco"),
        html.Div(className="Logo_ANID"),
        html.H2('Análisis Prescriptivo basado en Machine Learning para la operación de plantas de tablero contrachapado de alta producción de pino radiata', className = "nombre_proyecto"),
        html.H2('4.0', className = "numero_proyecto"),
        html.H2('Proyecto FONDEF ID22i10123', className = "codigo_proyecto"),
        #widget_fecha("custom-datepicker")
                            ],style = {'background': '#DFD1A7','height': '100vh'}
                            )
    return recomendacion
