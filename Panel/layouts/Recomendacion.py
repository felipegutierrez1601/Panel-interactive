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

datos = [{"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "2","ID_tabla_variable": "Tiempo Macerado_2", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "3","ID_tabla_variable": "Tiempo Macerado_3", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "4","ID_tabla_variable": "Tiempo Macerado_4", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "5","ID_tabla_variable": "Tiempo Macerado_5", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"},
         {"ID_tabla_jerarquia": "1","ID_tabla_variable": "Tiempo Macerado", "ID_tabla_tinicial": "10/12/10 15:54:30", "ID_tabla_final": "10/12/10 15:55:30", "ID_tabla_valor": "15", "ID_tabla_linfeior": "12","ID_tabla_lsuperior":"18", "ID_tabla_uom":"H"}]

marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
marks[1440] = '24:00'  # Agregar marca para las 24:00

muestras=['Calidad Chapa', 'Calidad Tablero', 'Meta']

garfico_cantidad = go.Figure(data=[
    go.Bar(name='Cumple', x=muestras, y=[20, 14, 23], marker_color = "#08AA49"),
    go.Bar(name='No Cumple', x=muestras, y=[12, 18, 29], marker_color = '#D20101')])

garfico_cantidad.update_traces(marker_line_width=1.5, opacity=1)

garfico_cantidad.update_layout(
    xaxis_title='Categoria',
    yaxis_title='Cantidad',
    showlegend=False,
    margin=dict(l=0, r=0, t=30, b=0),  # Elimina márgenes
    paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
    plot_bgcolor='#E0DEDE',   # Fondo de la gráfica transparente
    xaxis=dict(
        showline=True,  # Elimina la línea del eje x
        zeroline=True   # Elimina la línea cero
    ),
    yaxis=dict(
        showline=True,  # Elimina la línea del eje y
        zeroline=True   # Elimina la línea cero
    ),
    width=300,height=310,

    font=dict(
        family="Arimo ",   # Fuente del texto
        size=10,          # Tamaño del texto
        color="#000000"     # Color del texto
    ),
    title={
        'text': 'Acumulado Calidad',
        'font': {'size': 15},
        'x': 0.5,  # Centramos el título
        'xanchor': 'center'  # Alineación del título en el centro
            },
    barmode='group')



def grafico_indicador_movile(id,label,style_edit):
    alpha = dbc.Row([
            dbc.Col(daq.LEDDisplay(id = id,label=label,value=4 ,size=20,color="#000000", className = "CAJAS"),md = 1),
            ], style = style_edit)
    return alpha


def create_layout(app):
    marks = {i*60: f'{i:02}:00' for i in range(0, 25, 6)}
    marks[1440] = '24:00'  # Agregar marca para las 24:00
    now = datetime.now()
    recomendacion =html.Div([
       html.Div([
                    dcc.Location(id='navegador',refresh=False),
                    html.Div([
                        dcc.Link(
                            [
                                html.Img(src='/assets/home_2.png'),  # Imagen como icono
                            ],
                            href='/Principal',className='icon-link'),
                        html.Div(dcc.Link('Simulación', href='/Simulacion',id='link-2'),className='link', style={'margin-left':442}),
                        html.Div(dcc.Link('Recomendación', href='/Recomendacion',id='link-1'),className ='link2'),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo',id='link-3'),style= {'margin-left' : 305,'margin-top':'2px','font-family': 'Scene', 'padding': '2px' '5px','background-color': '#9AC4EE','border-radius': '15px','border': '2px solid #000000','width':'135px','font-size': '1px','height': '37px'}),
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
            html.H2('Calidad Chapa', className = "nombre_chapa"),
            grafico_indicador_movile("led","Cantidad",{'margin-top' : 70,'margin-left': 155,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            html.H2('Objetivo', className = "objetivo_chapa"),
            dbc.Badge("Cumple", color="#08AA49",className="Aprobado_chapa"),
            dbc.Button("Revisar", color="secondary", className="Revisar_chapa"),
                        ]
            ), className = "recomendacion_card_2"),
        
        dbc.Card(html.Div([

            html.H2('Calidad Tablero', className = "nombre_tablero"),
            grafico_indicador_movile("led","Cantidad",{'margin-top' : 70,'margin-left': 155,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            html.H2('Objetivo', className = "objetivo_tablero"),
            dbc.Badge("No Cumple", color="#D20101",className="Rechazo_tablero"),
            dbc.Button("Revisar", color="secondary", className="Revisar_tablero"),
                     ]
            ), className = "recomendacion_card_3"),
        
        dbc.Card(html.Div(
            [
            html.H2('Meta', className = "nombre_meta"),
            grafico_indicador_movile("led","Cantidad",{'margin-top' : 70,'margin-left': 155,'margin-right': 0,'width': 160,'height': 100,'textAlign': 'left', 'position': 'absolute'}),
            html.H2('Objetivo', className = "objetivo_meta"),
            dbc.Badge("Cumple", color="#08AA49",className="Aprobado_meta"),
            dbc.Button("Revisar", color="secondary", className="Revisar_meta"),            ]
            ), className = "recomendacion_card_4"),
        html.Div(className="vertical-line"),
        
        dbc.Card(html.Div(
            [
            dcc.Graph(config = {"displayModeBar": False},figure = garfico_cantidad,className = 'grafico_cantidad_kpi')
            ]
            ), className = "recomendacion_card_5"),
        dbc.Card(html.Div([
            html.H2('Variables', className = "revisa_variables"),
            dbc.DropdownMenu(label="Proceso",direction="down",className="custom-dropdown"),
            dbc.DropdownMenu(label="Máquina",direction="down",className="custom-dropdown2"),
            html.Div(id='output-container'),  # Placeholder para mostrar salida seleccionada
            dash_table.DataTable(data = datos,sort_action="native" ,columns=[{"name": "Jerarquía", "id": "ID_tabla_jerarquia"},{"name": "Variable", "id": "ID_tabla_variable"},{"name": "Máquina", "id": "ID_tabla_maquina"},{"name": "Tiempo inicial", "id": "ID_tabla_tinicial"},{"name": "Tiempo Final", "id": "ID_tabla_final"},{"name": "Valor", "id": "ID_tabla_valor"},{"name": "Limite inferior", "id": "ID_tabla_linfeior"},{"name": "Limite superior", "id": "ID_tabla_lsuperior"},{"name": "UOM", "id": "ID_tabla_uom"}],
                        style_table={'height': '242px', "width": "913px","position": "absolute", "margin-left": "150px", "margin-right": "1px", "margin-top": "100px", 'overflowY': 'auto'},
                        style_cell = {'border': '2px solid ',"background-color": "#F7FBFF", "font-size": "13px", "color": "#000000", "text-align": "center"},
                        style_header = {"background-color": "#9AC4EE", "color": "#000000", "text-align": "center"},
                        style_data_conditional=[{'if': {'row_index': 'odd'},  # Apply zebra striping
                                            'backgroundColor': '#F7FBFF'}],
                        page_action='none',),
            dbc.Button("Panel", color="secondary",outline=True, className="Revisar_panel"),]
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
                id='Calendario2',
                min_date_allowed=date(1995, 12, 12),
                max_date_allowed=date(2050, 12, 12),
                date = now.strftime("%Y-%m-%d"),
                display_format='YYYY-MM-DD',
                className='custom-datepicker_2'),

                            ],style = {'background': '#FFFFFF','height': '100vh','posicion': 'absolute'}
                            )
    return recomendacion
