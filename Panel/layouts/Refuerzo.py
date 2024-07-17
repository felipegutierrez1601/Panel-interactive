from dash import html, dcc, dash_table
import plotly.express as px
from data_loader import load_data
import dash_daq as daq
import dash_bootstrap_components as dbc
#from utils import widget_fecha
from datetime import datetime
from datetime import date
import plotly.graph_objects as go #Módulo para crear gráficos
import plotly.express as px #Módulo para crear gráficos
"""
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
    ])"""

def create_layout(app):

    refuerzo = html.Div([

        html.Div([
                    dcc.Location(id='navegador',refresh=False),
                    html.Div([
                        dcc.Link(
                            [
                                html.Img(src='/assets/home_2.png'),  # Imagen como icono
                            ],
                            href='/Principal',className='icon-link'),
                        html.Div(dcc.Link('Simulación', href='/Simulacion',id='link-2'),className='link',style={'margin-left':252}),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo',id='link-1'),className ='link2'),
                        html.Div(dcc.Link('Recomendación', href='/Recomendacion',id='link-3'),style= {'margin-left' : 420,'margin-top':'2px','font-family': 'Scene', 'padding': '2px' '5px','background-color': '#9AC4EE','border-radius': '15px','border': '2px solid #000000','width':'175px','font-size': '1px','height': '37px'}),
                    ], id='link-container', className='link-container')
                ]),
                        ],style = {'background': '#FFFFFF','height': '100vh','posicion': 'absolute'})

    return refuerzo