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

datos = [{"ID_tabla_jerarquia": "","ID_tabla_variable": "", "ID_tabla_tinicial": "", "ID_tabla_final": "", "ID_tabla_valor": "", "ID_tabla_linfeior": "","ID_tabla_lsuperior":"", "ID_tabla_uom":""},
        ]

marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
marks[1440] = '24:00'  # Agregar marca para las 24:00


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
    width=300,height=240,

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
    width=300,height=240,

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
        dbc.Card(html.Div([

                        dcc.Location(id='navegador',refresh=False),
                        dcc.Interval(id='intervalo',interval=10000,n_intervals=0),
                        html.Div([
                            dcc.Link(
                                [
                                    html.Img(src='/assets/home_2.png'),  # Imagen como icono
                                ],
                                href='/Principal',className='icon-link')]),
                        html.Div(dcc.Link('Simulación', href='/Simulacion',id='link-2'),className='link', style={'margin-left':100},title='Vista Simulación'),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo',id='link-1'),className ='link2',title='Vista Refuerzo'),
                        html.Div(dcc.Link('Predicción', href='/Recomendacion',id='link-3'),style= {'margin-left' : 100,'margin-top':'210px','font-family': 'Scene', 'padding': '2px 0px','background-color': '#FFFFFF','border-radius': '15px','border': '2px solid #000000','width':'160px','font-size': '1px','height': '37px'},title='Vista Recomendación'),

                            ]),
                className = "recomendacion_card_5" ),
        dbc.Card(html.Div([
            html.H2('Calidad S24', className = "nombre_S24"),
            grafico_indicador_movile("S24","No Cumple",{'margin-top' : 50,'margin-left': 1,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            #html.H2('Objetivo', className = "objetivo_S24"),
            #dbc.Badge("Cumple",id = 'Estado_s24', color="#08AA49",className="estado_"),
            dbc.Button("Revisar",id = 'Revisar_s24', color="secondary", className="Revisar_S24"),
                        ]
            ),id = 'Estado_s24',className = "recomendacion_card_2"),
        
        dbc.Card(html.Div([

            html.H2('Calidad S15', className = "nombre_S15"),
            grafico_indicador_movile("S15","No Cumple",{'margin-top' : 50,'margin-left': 1,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            #html.H2('Objetivo', className = "objetivo_S15"),
            #dbc.Badge("No Cumple",id = 'Estado_s15', color="#D20101",className="estado_"),
            dbc.Button("Revisar", color="secondary",id = 'Revisar_s15', className="Revisar_S15"),
                     ]
            ),id = 'Estado_s15' ,className = "recomendacion_card_3"),
        
        dbc.Card(html.Div(
            [
            html.H2('Calidad S18', className = "nombre_S18"),
            grafico_indicador_movile("S18","No Cumple",{'margin-top' : 50,'margin-left': 1,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            #html.H2('Objetivo', className = "objetivo_S18"),
            #dbc.Badge("Cumple",id = 'Estado_s18' ,color="#08AA49",className="estado_"),
            dbc.Button("Revisar",id = 'Revisar_s18', color="secondary", className="Revisar_S18"),            ]
            ), id = 'Estado_s18',className = "recomendacion_card_4"),
        
        dbc.Card(html.Div([
            html.H2('Importancia Variables', className = "impo_variables",id = 'titulo_variables'),
            #html.H2('Límites Variables', className = "limi_variables"),
            dcc.Graph(id='Va_importantes',config = {"displayModeBar": False},figure = garfico_features,className = 'grafico_features'),
            dcc.Graph(id='Va_importantes_2',config = {"displayModeBar": False},figure = garfico_features2,className = 'grafico_features2'),
            html.Div(id='output-container'),  # Placeholder para mostrar salida seleccionada
            dash_table.DataTable(id= 'tabla_rangos',data = datos ,columns=[{"name": "Variable", "id": "ID_tabla_variable"},{"name": "Predicción", "id": "ID_tabla_objetivo"},{"name": "Importancia [%]", "id": "ID_tabla_jerarquia_porcentaje"},{"name": "Máquina", "id": "ID_tabla_maquina"},{"name": "Ult. Valor", "id": "ID_tabla_valor"},{"name": "Lim. Inferior", "id": "ID_tabla_inferior"},{"name": "Lim. Superior", "id": "ID_tabla_superior"},{"name": "Unidad", "id": "ID_tabla_uom"}],
                        style_table={'height': '212px', "width": "484px","position": "absolute", "margin-left": "655px", "margin-right": "0px", "margin-top": "40px", 'overflowY': 'auto'},
                        style_cell = {'border': '2px solid #FFFFFF ',"background-color": "#121420", "font-size": "13px", "color": "#FFFFFF", "text-align": "center"},
                        style_header = {"background-color": "#343434", "color": "#FFFFFF", "text-align": "center",'overflowY': 'auto', 'overflowX': 'auto'},
                        style_data={'border': '1px solid #FFFFFF'},
                        style_data_conditional=[{'if': {'row_index': 'odd'},  # Apply zebra striping
                                            'backgroundColor': '#000000'},
                                            {'if': {'column_id': 'ID_tabla_jerarquia_porcentaje'},  # Apply zebra striping
                                                'width': '120px'},
                                            {'if': {'column_id':'ID_tabla_uom'},  # Apply zebra striping
                                                'width': '150px'},
                                            {'if': {'column_id':'ID_tabla_variable'},  # Apply zebra striping
                                                'width': '150px'},
                                            {'if': {'column_id':'ID_tabla_objetivo'},  # Apply zebra striping
                                                'width': '100px'},
                                            {'if': {'column_id':'ID_tabla_maquina'},  # Apply zebra striping
                                                'width': '80px'},
                                            {'if': {'column_id':'ID_tabla_valor'},  # Apply zebra striping
                                                'width': '100px'},
                                            {'if': {'column_id':'ID_tabla_inferior'},  # Apply zebra striping
                                                'width': '100px'},
                                            {'if': {'column_id':'ID_tabla_superior'},  # Apply zebra striping
                                                'width': '100px'}    ],
                        page_action='none',
                        sort_action='native',
                        sort_mode='multi',
                        fixed_rows={'headers': True}),
            dcc.Graph(id='gra_humedad_v1',config = {"displayModeBar": False},figure = garfico_features2,className = 'style_humedad_1'),
            dcc.Graph(id='gra_calidades',config = {"displayModeBar": False},figure = garfico_features2,className = 'style_calidad'),]
            ), className = "recomendacion_card_8"),
        html.Div(className="Logo_UBB")

                            ],style = {'background': '#121420','height': '100vh','posicion': 'absolute', 'Display':'flex','justify-content': 'center','align-items': 'center'}
                            )
    return recomendacion
