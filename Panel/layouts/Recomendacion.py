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

marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
marks[1440] = '24:00'  # Agregar marca para las 24:00

muestras=['Calidad Chapa', 'Calidad Tablero', 'Meta']

garfico_cantidad = go.Figure(data=[
    go.Bar(name='Cumplido', x=muestras, y=[20, 14, 23], marker_color = "#06544B"),
    go.Bar(name='Rechazo', x=muestras, y=[12, 18, 29], marker_color = '#D7263D')])

garfico_cantidad.update_traces(marker_line_width=1.5, opacity=0.6)

garfico_cantidad.update_layout(
    xaxis_title='Categoria',
    yaxis_title='Cantidad',
    margin=dict(l=0, r=0, t=0, b=0),  # Elimina márgenes
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
    plot_bgcolor='rgba(0,0,0,0)',   # Fondo de la gráfica transparente
    xaxis=dict(
        showline=False,  # Elimina la línea del eje x
        zeroline=False   # Elimina la línea cero
    ),
    yaxis=dict(
        showline=False,  # Elimina la línea del eje y
        zeroline=False   # Elimina la línea cero
    ),
    width=500,height=270,

    font=dict(
        family="Arimo ",   # Fuente del texto
        size=10,          # Tamaño del texto
        color="#DFD1A7"     # Color del texto
    ),
    barmode='group')



def grafico_indicador_movile(id,label,style_edit):
    alpha = dbc.Row([
            dbc.Col(daq.LEDDisplay(id = id,label=label,value=4 ,size=20,color="#000000", className = "CAJAS"),md = 1),
            dbc.Col(dcc.Graph(id = str('alert_' + id), config = {"displayModeBar": False},figure = indicador_targeta(10)),style = {'margin-top': -30,'textAlign': 'right','margin-left':-8,'line-left': 0,'position': 'relative','top': '44px','left': '38px'} , md = 1)
            ], style = style_edit)
    return alpha

def indicador_targeta(valor):
    fig = go.Figure()
    fig.add_trace(go.Indicator( mode = "delta",
        value = valor,
        delta = { 'reference': 2, 'relative': False ,'font':{'size':25}}))
    fig.update_layout(width=80,height=70, paper_bgcolor='#696158')
    return fig

def create_layout(app):
    marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
    marks[1440] = '24:00'  # Agregar marca para las 24:00
    now = datetime.now()
    recomendacion =html.Div([
        html.Div([
                    dcc.Location(id='navegador',refresh=False),
                    html.Div([
                        dcc.Link('Simulacion', href='/Simulacion',id='link-2', className='link'),
                        dcc.Link('Recomendacion', href='/Recomendacion',id='link-1', className='link'),
                        dcc.Link('Refuerzo', href='/Refuerzo',id='link-3', className='link')
                    ], id='link-container', className='link-container')
                ]),

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
        dbc.Card(html.Div(
            ), className = "recomendacion_card_6"),
        html.Div(className="Logo_UBB"),
        html.Div(className="Logo_Arauco"),
        html.Div(className="Logo_ANID"),
        html.H2('Análisis Prescriptivo basado en Machine Learning para la operación de plantas de tablero contrachapado de alta producción de pino radiata', className = "nombre_proyecto"),
        html.H2('4.0', className = "numero_proyecto"),
        html.H2('Proyecto FONDEF ID22i10123', className = "codigo_proyecto"),
        dcc.DatePickerSingle(
                id='Calendario',
                min_date_allowed=date(1995, 12, 12),
                max_date_allowed=date(2050, 12, 12),
                date = now.strftime("%Y-%m-%d"),
                display_format='YYYY-MM-DD',
                className='custom-datepicker'),
        dcc.DatePickerSingle(
                id='Calendario',
                min_date_allowed=date(1995, 12, 12),
                max_date_allowed=date(2050, 12, 12),
                date = now.strftime("%Y-%m-%d"),
                display_format='YYYY-MM-DD',
                className='custom-datepicker2'),
        dcc.RangeSlider(min=0,max=1440, marks=marks, value=[300, 900],className='custom-range-slider'),
        html.H2('Fecha', className = "nombre_fecha"),
        html.H2('Hora', className = "nombre_hora"),
        grafico_indicador_movile("led","Cantidad",{'margin-top' : -100,'margin-left': 560,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
        html.H2('Calidad Chapa', className = "nombre_chapa"),
        dbc.Badge("Cumplido", color="success",className="Aprobado_chapa"),
        html.H2('Objetivo', className = "objetivo_chapa"),
        dbc.Button("Revisar", color="secondary", className="Revisar_chapa"),
        html.H2('Calidad Tablero', className = "nombre_tablero"),
        grafico_indicador_movile("led","Cantidad",{'margin-top' : -100,'margin-left': 920,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
        dbc.Badge("Rechazo", color="danger",className="Rechazo_tablero"),
        html.H2('Objetivo', className = "objetivo_tablero"),
        dbc.Button("Revisar", color="secondary", className="Revisar_tablero"),
        html.H2('Meta', className = "nombre_meta"),
        grafico_indicador_movile("led","Cantidad",{'margin-top' : -100,'margin-left': 1285,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
        dbc.Badge("Cumplido", color="success",className="Aprobado_meta"),
        html.H2('Objetivo', className = "objetivo_meta"),
        dbc.Button("Revisar", color="secondary", className="Revisar_meta"),
        dcc.Graph(config = {"displayModeBar": False},figure = garfico_cantidad,className = 'grafico_cantidad_kpi')


                            ],style = {'background': '#DFD1A7','height': '100vh','posicion': 'absolute'}
                            )
    return recomendacion
