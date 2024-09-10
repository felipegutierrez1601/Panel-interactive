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

datos = [{"ID_tabla_jerarquia": "","ID_tabla_variable": "", "ID_tabla_tinicial": "", "ID_tabla_final": "", "ID_tabla_valor": "", "ID_tabla_linfeior": "","ID_tabla_lsuperior":"", "ID_tabla_uom":""},
        ]

marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
marks[1440] = '24:00'  # Agregar marca para las 24:00


muestras = ['Calidad Tablero','Rendimiento Planta','Meta']


garfico_cantidad = go.Figure(data=[
    go.Bar(name='Cumple', x=muestras, y=[0, 0, 0], marker_color = "#08AA49"),
    go.Bar(name='No Cumple', x=muestras, y=[0, 0, 0], marker_color = '#D20101')])

garfico_cantidad.update_traces(marker_line_width=1.5, opacity=1)

garfico_cantidad.update_layout(
    yaxis_title='Cantidad',
    showlegend=False,
    margin=dict(l=0, r=0, t=30, b=0),  # Elimina márgenes
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
    plot_bgcolor='#121420',   # Fondo de la gráfica transparente
    xaxis=dict(
        showline=True,  # Elimina la línea del eje x
        zeroline=True   # Elimina la línea cero
    ),
    yaxis=dict(
        showline=True,  # Elimina la línea del eje y
        zeroline=True   # Elimina la línea cero
    ),
    width=300,height=210,

    font=dict(
        family="Arimo ",   # Fuente del texto
        size=10,          # Tamaño del texto
        color="#FFFFFF"     # Color del texto
    ),
    title={
        'text': 'Calidad',
        'font': {'size': 15},
        'x': 0.5,  # Centramos el título
        'xanchor': 'center'  # Alineación del título en el centro
            },
    barmode='group')


garfico_features = go.Figure(data=[
    go.Bar(name='Cumple', x=[0,0,0,0,0,0,0,0,0,0,0], y=['V1','V2','v3','V4','V5','V6','V7','V8','v9','V10','V11',], marker_color = "#08AA49",orientation='h')])

garfico_features.update_traces(marker_line_width=1.5, opacity=1)

garfico_features.update_layout(
    showlegend=False,
    margin=dict(l=0, r=0, t=30, b=0),  # Elimina márgenes
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
    plot_bgcolor='#121420',   # Fondo de la gráfica transparente
    xaxis=dict(
        showline=True,  # Elimina la línea del eje x
        zeroline=True   # Elimina la línea cero
    ),
    yaxis=dict(
        showline=True,  # Elimina la línea del eje y
        zeroline=True   # Elimina la línea cero
    ),
    width=500,height=240,

    font=dict(
        family="Arimo ",   # Fuente del texto
        size=10,          # Tamaño del texto
        color="#FFFFFF"     # Color del texto
    ),
    barmode='group')

garfico_features2 = go.Figure(data=[
    go.Bar(name='Cumple', x=[0,0,0,0,0,0,0,0,0,0,0], y=['V1','V2','v3','V4','V5','V6','V7','V8','v9','V10','V11',], marker_color = "#08AA49",orientation='h')])

garfico_features2.update_traces(marker_line_width=1.5, opacity=1)

garfico_features2.update_layout(
    showlegend=False,
    margin=dict(l=0, r=0, t=30, b=0),  # Elimina márgenes
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
    plot_bgcolor='#121420',   # Fondo de la gráfica transparente
    xaxis=dict(
        showline=True,  # Elimina la línea del eje x
        zeroline=True   # Elimina la línea cero
    ),
    yaxis=dict(
        showline=True,  # Elimina la línea del eje y
        zeroline=True   # Elimina la línea cero
    ),
    width=500,height=240,

    font=dict(
        family="Arimo ",   # Fuente del texto
        size=10,          # Tamaño del texto
        color="#FFFFFF"     # Color del texto
    ),
    barmode='group')



def grafico_indicador_movile(id,label,style_edit):
    alpha = dbc.Row([
            dbc.Col(daq.LEDDisplay(id = str('alert_' + id),label=label,value=4 ,size=20,color="#000000", className = "CAJAS"),md = 1),
            ], style = style_edit)
    return alpha


def create_layout(app):

    marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
    marks[1440] = '24:00'  # Agregar marca para las 24:00
    now = datetime.now()
    recomendacion =html.Div([
       html.Div([
                    dcc.Location(id='navegador',refresh=False),
                    dcc.Interval(id='intervalo',interval=10000,n_intervals=0),
                    html.Div([
                        dcc.Link(
                            [
                                html.Img(src='/assets/home_2.png'),  # Imagen como icono
                            ],
                            href='/Principal',className='icon-link'),
                        html.Div(dcc.Link('Simulación', href='/Simulacion_tablero',id='link-2'),className='link', style={'margin-left':442},title='Vista Simulación'),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo_tablero',id='link-1'),className ='link2',title='Vista Refuerzo'),
                        html.Div(dcc.Link('Recomendación', href='/Recomendacion_tablero',id='link-3'),style= {'margin-left' : 248,'margin-top':'2px','font-family': 'Scene', 'padding': '2px 0px','background-color': '#FFFFFF','border-radius': '15px','border': '2px solid #000000','width':'195px','font-size': '1px','height': '37px'},title='Vista Recomendación'),
                    ], id='link-container', className='link-container')
                ]),

        dbc.Card(html.Div(

            [
            html.H2('Fecha', className = "nombre_fecha"),
            html.H2('Hora', className = "nombre_hora"),
            dcc.RangeSlider(min=0,max=1440, marks=marks, value=[300, 900],className='custom-range-slider'),

            ]
            ), className = "recomendacion_card_1"),
        dbc.Card(html.Div([
            html.H2('Calidad Tablero', className = "nombre_S24"),
            grafico_indicador_movile("calidad_tablero","Cantidad",{'margin-top' : 50,'margin-left': 1,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            #html.H2('Objetivo', className = "objetivo_S24"),
            #dbc.Badge("Cumple",id = 'Estado_s24', color="#08AA49",className="estado_"),
            dbc.Button("Revisar",id = 'Revisar_calidad_tablero', color="secondary", className="Revisar_S24"),
                        ]
            ),id = 'Estado_calidad_tablero',className = "recomendacion_card_2"),
        
        dbc.Card(html.Div([

            html.H2('Rendimiento Planta', className = "nombre_S15"),
            grafico_indicador_movile("rendimiento_planta","Cantidad",{'margin-top' : 50,'margin-left': 1,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            #html.H2('Objetivo', className = "objetivo_S15"),
            #dbc.Badge("No Cumple",id = 'Estado_s15', color="#D20101",className="estado_"),
            dbc.Button("Revisar", color="secondary",id = 'Revisar_rendimiento_planta', className="Revisar_S15"),
                     ]
            ),id = 'Estado_rendimiento_planta' ,className = "recomendacion_card_3"),
        
        dbc.Card(html.Div(
            [
            html.H2('Meta', className = "nombre_S18"),
            grafico_indicador_movile("meta","Cantidad",{'margin-top' : 50,'margin-left': 1,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            #html.H2('Objetivo', className = "objetivo_S18"),
            #dbc.Badge("Cumple",id = 'Estado_s18' ,color="#08AA49",className="estado_"),
            dbc.Button("Revisar",id = 'Revisar_meta', color="secondary", className="Revisar_S18"),            ]
            ), id = 'Estado_meta',className = "recomendacion_card_4"),

        dbc.Button("Detalles",id = 'id_revisar_panel', color="secondary",outline=True, className="Revisar_panel"),

        html.Div(className="vertical-line"),
        
        dbc.Card(html.Div(
            dcc.Graph(id='grafico_Tablero',config = {"displayModeBar": False},figure = garfico_cantidad,className = 'grafico_cantidad_kpi_tablero')
            ), className = "recomendacion_card_7"),
        dbc.Card(html.Div([
            html.H2('Importancia Variables', className = "impo_variables",id = 'titulo_variables'),
            #html.H2('Límites Variables', className = "limi_variables"),
            dcc.Graph(id='tablero_importantes',config = {"displayModeBar": False},figure = garfico_features,className = 'grafico_features'),
            dcc.Graph(id='tablero_importantes_2',config = {"displayModeBar": False},figure = garfico_features2,className = 'grafico_features2'),
            html.Div(id='output-container'),  # Placeholder para mostrar salida seleccionada
            dash_table.DataTable(id= 'tabla_rangos_tablero',data = datos,sort_action="native" ,columns=[{"name": "Porcentaje Objetivo", "id": "ID_tabla_jerarquia_porcentaje"},{"name": "Objetivo", "id": "ID_tabla_objetivo"},{"name": "Variable", "id": "ID_tabla_variable"},{"name": "Máquina", "id": "ID_tabla_maquina"},{"name": "Valor", "id": "ID_tabla_valor"},{"name": "Limite inferior", "id": "ID_tabla_inferior"},{"name": "Limite superior", "id": "ID_tabla_superior"},{"name": "UOM", "id": "ID_tabla_uom"}],
                        style_table={'height': '272px', "width": "1000px","position": "absolute", "margin-left": "80px", "margin-right": "1px", "margin-top": "260px", 'overflowY': 'auto'},
                        style_cell = {'border': '2px solid #FFFFFF ',"background-color": "#121420", "font-size": "13px", "color": "#FFFFFF", "text-align": "center"},
                        style_header = {"background-color": "#343434", "color": "#FFFFFF", "text-align": "center"},
                        style_data={'border': '1px solid #FFFFFF'},
                        style_data_conditional=[{'if': {'row_index': 'odd'},  # Apply zebra striping
                                                'backgroundColor': '#000000'},
                                                {'if': {'ID_tabla_jerarquia_porcentaje': 'Porcentaje Objetivo'},  # Apply zebra striping
                                                'width': '100px'}],
                        page_action='none',),
            dcc.Location(id="url2", refresh=True)]
            ), className = "recomendacion_card_8"),
        html.Div(className="Logo_UBB"),
        html.Div(className="Logo_Arauco"),
        html.Div(className="Logo_ANID"),
        html.H2('Análisis Prescriptivo basado en Machine Learning para la operación de plantas de tablero contrachapado de alta producción de pino radiata', className = "nombre_proyecto"),
        html.H2('4.0', className = "numero_proyecto"),
        html.H2('Proyecto FONDEF ID22i10123', className = "codigo_proyecto"),
        dcc.DatePickerSingle(
                id='Calendario_tablero',
                min_date_allowed=date(1995, 12, 12),
                max_date_allowed=date(2050, 12, 12),
                date = now.strftime("%Y-%m-%d"),
                display_format='YYYY-MM-DD',
                className='custom-datepicker'),
            dcc.DatePickerSingle(
                id='Calendario2_tablero',
                min_date_allowed=date(1995, 12, 12),
                max_date_allowed=date(2050, 12, 12),
                date = now.strftime("%Y-%m-%d"),
                display_format='YYYY-MM-DD',
                className='custom-datepicker_2'),

                            ],style = {'background': '#121420','height': '100vh','posicion': 'absolute'}
                            )
    return recomendacion
