from dash.dependencies import Input, Output,State
#from data_loader import load_data
import plotly.express as px
import pyodbc
import pandas as pd
import plotly.graph_objects as go #Módulo para crear gráficos
import dash

def register_callbacks_layout4(app):
    def load_data(consulta,database):
        mi_conexion = pyodbc.connect(
                    Trusted_Connection='No',
                    Authentication='ActiveDirectoryPassword',
                    UID='Felipe',
                    PWD= 'Fondef',
                    Driver='{SQL Server}',
                    Server='146.83.131.135',
                    Database=database)
        data = pd.read_sql(consulta, mi_conexion)
        return data

    def calcular_porcentaje(row,total_positivo,total_negativo):
        if row['Valor_Shap'] > 0:
            return (row['Valor_Shap'] / total_positivo) * 100
        elif row['Valor_Shap'] < 0:
            return (row['Valor_Shap'] / total_negativo) * 100
        else:
            return 0




    def grafico_importancia(x_data,y_data,z_data,direccion,lado,empuje):
        colors = ['#08AA49' if x > 0 else '#D20101' for x in x_data]
        garfico_features = go.Figure(data=[
                go.Bar(name='Cumple', x=z_data.abs(), y=y_data, marker_color = colors,orientation='h')])
        garfico_features.update_traces(marker_line_width=1.5, opacity=1)
        garfico_features.update_layout(
            xaxis_title=empuje,
            showlegend=False,
            margin=dict(l=0, r=0, t=30, b=0),  # Elimina márgenes
            paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
            plot_bgcolor='#121420',   # Fondo de la gráfica transparente
            xaxis=dict(
                showline=True,  # Elimina la línea del eje x
                zeroline=True,   # Elimina la línea cero
                autorange=direccion
            ),
            yaxis=dict(
                showline=True,  # Elimina la línea del eje y
                zeroline=True,   # Elimina la línea cero
                side=lado
            ),
            width=500,height=240,

            font=dict(
                family="Arimo ",   # Fuente del texto
                size=10,          # Tamaño del texto
                color="#FFFFFF"     # Color del texto
            ),
            barmode='group')
        return garfico_features

    def sharp(tabla):
        consulta = f"""
                        WITH Totales AS (
                        SELECT
                            SUM(CASE WHEN s.Valor_Shap > 0 THEN s.Valor_Shap ELSE 0 END) AS Total_Positivo,
                            SUM(CASE WHEN s.Valor_Shap < 0 THEN s.Valor_Shap ELSE 0 END) AS Total_Negativo
                        FROM {tabla} AS s
                    )
                    SELECT
                        v.Nombre_variable AS ID_tabla_variable,
                        v.Maquina AS ID_tabla_maquina,
                        ROUND(l.Value, 2) AS ID_tabla_valor,
                        v.Min AS ID_tabla_inferior,
                        v.Max AS ID_tabla_superior,
                        v.UOM AS ID_tabla_uom,
                        ROUND(
                            CASE
                                WHEN s.Valor_Shap > 0 THEN s.Valor_Shap / t.Total_Positivo * 100
                                WHEN s.Valor_Shap < 0 THEN s.Valor_Shap / t.Total_Negativo * 100
                                ELSE 0
                            END, 3
                        ) AS ID_tabla_jerarquia_porcentaje,
                        CASE
                            WHEN s.Valor_Shap > 0 THEN 'cumple'
                            WHEN s.Valor_Shap < 0 THEN 'no cumple'
                            ELSE 'indeterminado'
                        END AS ID_tabla_objetivo
                    FROM Variables v
                    JOIN Lecturas_Numericas_DT AS l ON v.ID_variable = l.ID_Variable
                    JOIN {tabla} AS s ON v.Descripcion = s.Variable_Shap
                    JOIN (
                        SELECT ID_Variable, MAX(TS) AS MaxTS
                        FROM Lecturas_Numericas_DT
                        GROUP BY ID_Variable
                    ) AS latest ON l.ID_Variable = latest.ID_Variable AND l.TS = latest.MaxTS
                    CROSS JOIN Totales t
                    ORDER BY ROUND(s.Valor_Shap, 2) DESC;"""

        data = load_data(consulta,'Arauco')
        data = data.to_dict(orient='records')
        return data


    @app.callback(
        Output('grafico_Tablero','figure'),

        [Input('Calendario2_tablero', 'date'),
         Input('Calendario_tablero', 'date')])

    def update_graph(start_date, end_date):
        if start_date > end_date:
            start_date, end_date = end_date, start_date
            consulta = f"""
            SELECT calidad_tablero,rendimiento_planta,meta
            FROM Lecturas_Resultados
            WHERE TS BETWEEN '{start_date}' AND '{end_date}'
            """
            cantidad = load_data(consulta,'UBB')


            
            garfico_cantidad = go.Figure(data=[
            go.Bar(name='Cumple', x=['Calidad Tablero','Rendimineto Planta','Meta'], y=[cantidad[cantidad['calidad_tablero'] == 'cumple'].shape[0],cantidad[cantidad['rendimiento_planta'] == 'cumple'].shape[0], cantidad[cantidad['meta'] == 'cumple'].shape[0] ], marker_color = "#08AA49"),
            go.Bar(name='No Cumple', x=['Calidad Tablero','Rendimineto Planta','Meta'], y=[cantidad[cantidad['calidad_tablero'] == 'No cumple'].shape[0],cantidad[cantidad['rendimiento_planta'] == 'No cumple'].shape[0], cantidad[cantidad['meta'] == 'No cumple'].shape[0] ], marker_color = "#D20101"),
            ])

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
                    'text': 'Predicción Calidad',
                    'font': {'size': 15},
                    'x': 0.55,  # Centramos el título
                    'xanchor': 'center'  # Alineación del título en el centro
                        },
                barmode='group')
        return garfico_cantidad



    @app.callback(
        [
        Output('Estado_calidad_tablero', 'style'),
        Output('Estado_rendimiento_planta', 'style'),
        Output('Estado_meta', 'style')],
        [Input('intervalo', 'interval')])

    def update_graph(*args):
        consulta = f"""
            SELECT TOP 1 calidad_tablero,rendimiento_planta,meta
            FROM Lecturas_Resultados
            ORDER BY TS DESC
        """
        Df = load_data(consulta, 'UBB')
        
        if not Df.empty:
            return [
                {"backgroundColor": "#08AA49"} if Df['calidad_tablero'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#D20101"},
                {"backgroundColor": "#08AA49"} if Df['rendimiento_planta'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#D20101"},
                {"backgroundColor": "#08AA49"} if Df['meta'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#D20101"},
            ]
        else:
            return {"backgroundColor": "#08AA49"} * 3


    @app.callback(
        [Output('alert_calidad_tablero', 'value'),
        Output('alert_rendimiento_planta', 'value'),
        Output('alert_meta', 'value')],
        [Input('intervalo', 'n_intervals')])
    def update_graph(intervalo):
        consulta = f"""
            SELECT TOP 2 calidad_tablero,rendimiento_planta,meta
            FROM Lecturas_Resultados
            order by TS DESC
            """
        Df = load_data(consulta,'UBB')
        ctablero =  Df[Df['calidad_tablero'].fillna('0') == 'No cumple'].shape[0] if not Df['calidad_tablero'].isnull().all() else 0
        rplanta =  Df[Df['rendimiento_planta'].fillna('0') == 'No cumple'].shape[0] if not Df['rendimiento_planta'].isnull().all() else 0
        meta =  Df[Df['meta'].fillna('0') == 'No cumple'].shape[0] if not Df['meta'].isnull().all() else 0

        return[ctablero,rplanta,meta]

    @app.callback(
        [Output('tablero_importantes', 'figure'),
        Output('tabla_rangos_tablero', 'data'),
        Output('tablero_importantes_2', 'figure')],


        [Input('Revisar_Revisar_calidad_tablero', 'n_clicks'),
        Input('Revisar_rendimiento_planta', 'n_clicks'),
        Input('Revisar_meta', 'n_clicks')],

        [State('alert_calidad_tablero', 'value'),
         State('alert_rendimiento_planta', 'value'),
         State('alert_meta', 'value')])

    def update_graph(Revisar_Revisar_calidad_tablero,Revisar_rendimiento_planta,Revisar_meta,alert_calidad_tablero,alert_rendimiento_planta,alert_meta):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'Revisar_Revisar_calidad_tablero':
            consulta = f"""
                SELECT Variable_Shap,
                Valor_Shap
                FROM Tablero_calidad_Shap 
                order by ABS(Valor_Shap) asc
                """
            feature_tablero = load_data(consulta,'Arauco')
            if int(alert_calidad_tablero) > -10:
                total_positivo = feature_tablero[feature_tablero['Valor_Shap'] > 0]['Valor_Shap'].sum()
                total_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]['Valor_Shap'].sum()
                feature_tablero['porcentaje'] = feature_tablero.apply(calcular_porcentaje, axis=1,args=(total_positivo, total_negativo))
                dataset_positivo = feature_tablero[feature_tablero['Valor_Shap'] >= 0]
                dataset_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]

                garfico_positivo = grafico_importancia(dataset_positivo['Valor_Shap'],dataset_positivo['Variable_Shap'],dataset_positivo['porcentaje'],True,'right',f'% Empuje Positivo')
                garfico_negativo = grafico_importancia(dataset_negativo['Valor_Shap'],dataset_negativo['Variable_Shap'],dataset_negativo['porcentaje'],'reversed','left',f'% Empuje Negativo')
                datos = sharp('Tablero_calidad_Shap')
                return [garfico_negativo,datos,garfico_positivo]


        elif button_id == 'Revisar_rendimiento_planta' :
            consulta = f"""
                SELECT Variable_Shap,
                Valor_Shap
                FROM Tablero_rendimiento_Shap 
                order by ABS(Valor_Shap) asc
                """
            feature_tablero = load_data(consulta,'Arauco')
            if int(alert_rendimiento_planta) >= 0:
                total_positivo = feature_tablero[feature_tablero['Valor_Shap'] > 0]['Valor_Shap'].sum()
                total_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]['Valor_Shap'].sum()
                feature_tablero['porcentaje'] = feature_tablero.apply(calcular_porcentaje, axis=1,args=(total_positivo, total_negativo))
                dataset_positivo = feature_tablero[feature_tablero['Valor_Shap'] >= 0]
                dataset_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]

                garfico_positivo = grafico_importancia(dataset_positivo['Valor_Shap'],dataset_positivo['Variable_Shap'],dataset_positivo['porcentaje'],True,'right',f'% Empuje Positivo')
                garfico_negativo = grafico_importancia(dataset_negativo['Valor_Shap'],dataset_negativo['Variable_Shap'],dataset_negativo['porcentaje'],'reversed','left',f'% Empuje Negativo')
                datos = sharp('Tablero_rendimiento_Shap')
                return [garfico_negativo,datos,garfico_positivo]


        elif button_id == 'Revisar_meta':
            consulta = f"""
                SELECT Variable_Shap,
                Valor_Shap
                FROM meta_Shap 
                order by ABS(Valor_Shap) asc
                """
            feature_tablero = load_data(consulta,'Arauco')
            if int(alert_meta) >= 0:
                total_positivo = feature_tablero[feature_tablero['Valor_Shap'] > 0]['Valor_Shap'].sum()
                total_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]['Valor_Shap'].sum()
                feature_tablero['porcentaje'] = feature_tablero.apply(calcular_porcentaje, axis=1,args=(total_positivo, total_negativo))
                dataset_positivo = feature_tablero[feature_tablero['Valor_Shap'] >= 0]
                dataset_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]

                garfico_positivo = grafico_importancia(dataset_positivo['Valor_Shap'],dataset_positivo['Variable_Shap'],dataset_positivo['porcentaje'],True,'right',f'% Empuje Positivo')
                garfico_negativo = grafico_importancia(dataset_negativo['Valor_Shap'],dataset_negativo['Variable_Shap'],dataset_negativo['porcentaje'],'reversed','left',f'% Empuje Negativo')
                datos = sharp('meta_Shap')
                return [garfico_negativo,datos,garfico_positivo]
  

        else:
            return dash.no_update