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
"""

def create_layout(app):
    principal= html.Div([

        dbc.Card([html.Div([
            dcc.Link('Chapa', href='/Recomendacion',className= "mace_torno_secado")
                            ],className = 'mace_torno_div'),
        dcc.Link('Recomendación', href='/Recomendacion',className= "_recomendacion"),
        dcc.Link('Simulación', href='/Simulacion',className= "_simulacion"),
        dcc.Link('Refuerzo', href='/Refuerzo',className= "_refuerzo"),
        ], className = "principal_card_1"),
        dbc.Card([html.Div([
            dcc.Link('Tablero', href='/Recomendacion_tablero',className= "enco_empaque")
                            ], className = 'secado_div'),
        dcc.Link('Recomendación', href='/Recomendacion_tablero',className= "_recomendacion"),
        dcc.Link('Simulación', href='/Simulacion_tablero',className= "_simulacion"),
        dcc.Link('Refuerzo', href='/Refuerzo_tablero',className= "_refuerzo"),
        ], className = "principal_card_2"),
        html.Div(className="Logo_UBB"),
        html.Div(className="Logo_Arauco"),
        html.Div(className="Logo_ANID"),
        html.H2('Análisis Prescriptivo basado en Machine Learning para la operación de plantas de tablero contrachapado de alta producción de pino radiata', className = "nombre_proyecto"),
        html.H2('4.0', className = "numero_proyecto"),
        html.H2('Proyecto FONDEF ID22i10123', className = "codigo_proyecto")] 

        ,style = {'background': '#FFFFFF','height': '100vh','posicion': 'absolute'})
    return principal