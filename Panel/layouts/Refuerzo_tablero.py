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
                        html.Div(dcc.Link('Recomendación', href='/Recomendacion_tablero',id='link-2'),className='link',style={'margin-left':240}),
                        html.Div(dcc.Link('Simulación', href='Simulacion_tablero',id='link-1'),className ='link2',style={'margin-left':446}),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo_tablero',id='link-3'),style= {'margin-left' : 100,'margin-top':'2px','font-family': 'Scene', 'padding': '2px' '5px','background-color': '#FFFFFF','border-radius': '15px','border': '2px solid #000000','width':'140px','font-size': '1px','height': '37px'}),
                    ], id='link-container', className='link-container')
                ]),
                        ],style = {'background': '#FFFFFF','height': '100vh','posicion': 'absolute'})

    return refuerzo