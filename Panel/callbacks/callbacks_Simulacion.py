from dash.dependencies import Input, Output,State,ALL
#from data_loader import load_data
import plotly.express as px
import pyodbc
import pandas as pd
import plotly.graph_objects as go #Módulo para crear gráficos
import dash
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
import model_simul as ms

columnas = []

def register_callbacks_layout2(app):

    def load_data(consulta,database):
        mi_conexion = pyodbc.connect(
                    Trusted_Connection='No',
                    Authentication='ActiveDirectoryPassword',
                    UID='',
                    PWD= '',
                    Driver='{SQL Server}',
                    Server='146.83.131.135',
                    Database=database)
        data = pd.read_sql(consulta, mi_conexion)
        return data

    def create_table(tabla):
        consulta = f"""WITH UltimosValores AS (
                        SELECT ID_Variable, Value,
                               ROW_NUMBER() OVER (PARTITION BY ID_Variable ORDER BY TS DESC) AS rn
                        FROM Lecturas_numericas_DT
                    ),
                    ShapOrdenadas AS (
                        SELECT Variable_Shap, 
                               ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS orden
                        FROM {tabla}
                    )
                    SELECT 
                        v.Nombre_variable AS variable, 
                        ROUND(ISNULL(u.Value, 0),1) AS Value,
                        v.Maquina,
                        v.Min,
                        v.Max,
                        v.[Filtro inferior DT],
                        v.[Filtro superior DT],
                        v.Descripcion
                    FROM ShapOrdenadas s
                    JOIN Variables v 
                        ON v.Descripcion = s.Variable_Shap
                    LEFT JOIN UltimosValores u
                        ON v.ID_Variable = u.ID_Variable
                        AND u.rn = 1
                    ORDER BY s.orden;"""
        data = load_data(consulta,'Arauco')
        return data

    def create_widget(df):
        botones = []
        margen_left = 0
        margen_top = 0
        for index, fila in df.iterrows():
            marks={fila.iloc[3]: {'label': 'L.I', 'style': {'color': '#79af61'}}, 
                   fila.iloc[4]: {'label': 'L.S', 'style': {'color': '#79af61'}}}
            estilo = {'margin-left':margen_left,'margin-top':margen_top}
            # Personaliza el botón según tus necesidades
            boton = html.Div([
                    daq.LEDDisplay(id = {'type': 'LEDDisplay', 'index': int(index + len(df))},label=str(fila.iloc[0]),value=fila.iloc[1] ,size=10,color="#000000"),
                    dcc.Slider(fila.iloc[5], fila.iloc[6],float(fila.iloc[6] - fila.iloc[5])/100, marks = marks,tooltip={"always_visible": False,"template":"{value}"},vertical=True,className='sound-slider',id = {'type': 'Slider', 'index': int(index + len(df))},value = fila.iloc[1])
                    ],className = 'tarjeta_control',style = estilo,) 
            margen_left = margen_left + 150 
            margen_top = -290
            botones.append(boton)
        return botones



    @app.callback(
    [Output("simu_car2", "style"),
    Output("simu_car3", "style"),
    Output("simu_car4", "style"),
    Output("simu_car5", "style"),
    Output("simu_car6", "style"),],
    [Input("simu_car2", "n_clicks"),
    Input("simu_car3", "n_clicks"),
    Input("simu_car4", "n_clicks"),
    Input("simu_car5", "n_clicks"),
    Input("simu_car6", "n_clicks")])


    def display_clicks(*args):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        consulta = f"""
            SELECT TOP 1 calidad_chapa_s24, calidad_chapa_s18, calidad_chapa_s15, calidad_chapa_general, rendimiento_clear
            FROM Lecturas_Resultados
            ORDER BY TS DESC
        """
        Df = load_data(consulta, 'UBB')

        if button_id == 'simu_car2':
            if not Df.empty:
                return [
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_s24'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"}
                ]
            else:
                return {"backgroundColor": "#08AA49"} * 5

        elif button_id == 'simu_car3':
            if not Df.empty:
                return [
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_s15'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"}
                ]
            else:
                return {"backgroundColor": "#08AA49"} * 5


        elif button_id == 'simu_car4':
            if not Df.empty:
                return [
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_s18'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"}
                ]
            else:
                return {"backgroundColor": "#08AA49"} * 5

        elif button_id == 'simu_car5':
            if not Df.empty:
                return [
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_general'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
                {"backgroundColor": "#121420"}
                ]
            else:
                return {"backgroundColor": "#08AA49"} * 5

        elif button_id == 'simu_car6':
            if not Df.empty:
                return [
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#121420"},
                {"backgroundColor": "#79af61"} if Df['rendimiento_clear'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"}
                ]
            else:
                return {"backgroundColor": "#08AA49"} * 5

    

    @app.callback(
    [Output("control_panel1", "children"),
    Output("control_panel2", "children")],
    [Input("simu_car2", "n_clicks"),
    Input("simu_car3", "n_clicks"),
    Input("simu_car4", "n_clicks"),
    Input("simu_car5", "n_clicks"),
    Input("simu_car6", "n_clicks")])

    def display_clicks(*args):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        global columnas

        if button_id == 'simu_car2':
            df = create_table('S24_Shap')
            columnas = df['Descripcion'].to_list()
            botones = create_widget(df[:7])
            botones2 = create_widget(df[7:])
            return [botones,botones2]

        elif button_id == 'simu_car3':
            df = create_table('S15_Shap')
            columnas = df['Descripcion'].to_list()
            botones = create_widget(df[:7])
            botones2 = create_widget(df[7:])
            return [botones,botones2]

        elif button_id == 'simu_car4':
            df = create_table('S18_Shap')
            columnas = df['Descripcion'].to_list()
            botones = create_widget(df[:7])
            botones2 = create_widget(df[7:])
            return [botones,botones2]

        elif button_id == 'simu_car5':
            df = create_table('chapa_G_Shap')
            columnas = df['Descripcion'].to_list()
            botones = create_widget(df[:7])
            botones2 = create_widget(df[7:])
            return [botones,botones2]

        elif button_id == 'simu_car6':
            df = create_table('chapa_G_clear_Shap')
            columnas = df['Descripcion'].to_list()
            botones = create_widget(df[:7])
            botones2 = create_widget(df[7:])
            return [botones,botones2]


    

    @app.callback(
    Output({'type': 'LEDDisplay', 'index': ALL}, 'value'),
    [Input({'type': 'Slider', 'index': ALL}, 'value')])

    def actualizar_led_displays(slider_values):
        # Regresa una lista de valores que corresponde al Output de cada LEDDisplay
        return [f"{valor:.2f}" for valor in slider_values]

    @app.callback(
    [Output('Estado_nombre', 'children'),
    Output('Estado_simu', 'style')],  # Este Output puede ser solo para indicar que se ha guardado la fila
    Input('simu_car7', 'n_clicks'),  # Botón que guarda los valores
    State({'type': 'Slider', 'index': ALL}, 'value') ) # Recupera los valores actuales de los sliders

    def guardar_valores(n_clicks, slider_values):
        global columnas
        if n_clicks != None:
            nueva_fila = pd.Series(slider_values)
            data = pd.DataFrame(nueva_fila).T
            data.columns = columnas
            last_20_columns = data.iloc[:, -20:]
            data['Promedio_Hora_Macerado'] = last_20_columns.mean(axis=1)
            data.drop(last_20_columns.columns, axis=1, inplace=True)
            salida = ms.main('calidad_chapa_s24',data)
            print(salida)

