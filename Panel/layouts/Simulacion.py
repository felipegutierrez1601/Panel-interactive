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

marks={2: {'label': 'L.I', 'style': {'color': '#79af61'}}, 
       3: {'label': 'L.S', 'style': {'color': '#79af61'}}}

def create_layout(app):

    simulacion = html.Div([

        html.Div([
                    dcc.Location(id='navegador',refresh=False),
                    html.Div([
                        dcc.Link(
                            [
                                html.Img(src='/assets/home_2.png'),  # Imagen como icono
                            ],
                            href='/Principal',className='icon-link'),
                        html.Div(dcc.Link('Recomendación', href='/Recomendacion',id='link-2'),className='link',style={'margin-left':249}),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo',id='link-1'),className ='link2'),
                        html.Div(dcc.Link('Simulación', href='Simulacion',id='link-3'),style= {'margin-left' : 453,'margin-top':'2px','font-family': 'Scene', 'padding': '2px' '5px','background-color': '#FFFFFF','border-radius': '15px','border': '2px solid #000000','width':'150px','font-size': '1px','height': '37px'}),
                    ], id='link-container', className='link-container')
                ]),
        dbc.Card([
            html.Div([
                        dbc.Button(html.Div([
                            html.H2('Calidad S24', className = "nombre_S24",style = {'margin-top':'-32px'})]),id = 'simu_car2',className = "simulacion_card_2",),
                        dbc.Button(html.Div([

                            html.H2('Calidad S15', className = "nombre_S15",style = {'margin-top':'-32px'})]),id = 'simu_car3' ,className = "simulacion_card_3"),

                        dbc.Button(html.Div([

                            html.H2('Calidad S18', className = "nombre_S18",style = {'margin-top':'-32px'})]),id = 'simu_car4' ,className = "simulacion_card_4"),
                        dbc.Button(html.Div([

                            html.H2('Calidad Secado', className = "nombre_chapa",style = {'margin-top':'-32px'})]),id = 'simu_car5' ,className = "simulacion_card_5"),
                        dbc.Button(html.Div([

                            html.H2('Rendimiento Clear', className = "nombre_clear",style = {'margin-top':'-32px'})]),id = 'simu_car6' ,className = "simulacion_card_6"),

                            html.Div([],id="control_panel1",className = 'control_panel1')]),
            html.Div([],id="control_panel2",className = 'control_panel2'),
            dbc.Button(html.Div([html.H2('Aceptar', className = "nombre_S24",style = {'margin-top':'-10px'})]),id = 'simu_car7',className = "simulacion_card_7"),
            dbc.Card(html.H2('No Data', className = "nombre_S15",style = {'margin-top':'30px','margin-left':'65px'},id = 'Estado_nombre'),id = 'Estado_simu' ,className = "simulacion_card_8")
                    ], className = 'tarjeta_simu_1'),


        html.Div(className="Logo_UBB"),
        html.Div(className="Logo_Arauco"),
        html.Div(className="Logo_ANID"),
        html.H2('Análisis Prescriptivo basado en Machine Learning para la operación de plantas de tablero contrachapado de alta producción de pino radiata', className = "nombre_proyecto"),
        html.H2('4.0', className = "numero_proyecto"),
        html.H2('Proyecto FONDEF ID22i10123', className = "codigo_proyecto")
                        ],style = {'background': '#121420','height': '100vh','posicion': 'absolute'})

    return simulacion