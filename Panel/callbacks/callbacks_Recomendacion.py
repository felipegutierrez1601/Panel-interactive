from dash.dependencies import Input, Output,State
#from data_loader import load_data
import plotly.express as px
import pyodbc
import pandas as pd
import plotly.graph_objects as go #Módulo para crear gráficos
import dash

def register_callbacks_layout1(app):
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

    def calcular_porcentaje(row,total_positivo,total_negativo):
        if row['Valor_Shap'] > 0:
            return (row['Valor_Shap'] / total_positivo) * 100
        elif row['Valor_Shap'] < 0:
            return (row['Valor_Shap'] / total_negativo) * 100
        else:
            return 0

    def grafico_humedad_calidad(datos,titulo):
        datos_5 = datos.iloc[:, 1:]
        datos_5['Suma_Total'] = datos_5.sum(axis=1)
        for col in datos_5.columns:
            datos_5[f'{col}_percent'] = datos_5[col] / datos_5['Suma_Total'] * 100
        datos_5 = datos_5.drop(['Suma_Total','Suma_Total_percent'], axis=1)

        # Crear gráfico de barras apiladas solo con los primeros 5 registros
        fig = go.Figure()

        # Añadir barras para cada columna de humedad
        for col in datos_5.filter(like='_percent').columns:
            fig.add_trace(go.Bar(
                x=datos['TS'], 
                y=datos_5[col].round(1), 
                name=col[:-8],
                hovertemplate='%{y:.1f}%',  # Mostrar porcentaje en el hover
                texttemplate='%{y:.1f}%',  # Mostrar el valor en la barra
                textposition='inside',
                hoverinfo='text',
                opacity=0.1
            ))

        # Establecer diseño del gráfico
        fig.update_layout(
            barmode='stack',  # Barras apiladas
            title={'text': titulo, 
                    'x': 0.5,  # Centrar el título
                    'xanchor': 'center',
                    'yanchor': 'top'},
            xaxis_title='Fecha (TS)',
            yaxis_title='% Total',
            hovermode="x unified",  # Mostrar todas las barras al mismo tiempo al pasar el mouse
            margin=dict(l=0, r=0, t=30, b=0),  # Elimina márgenes
            paper_bgcolor='rgba(0,0,0,0)',  # Fondo del contenedor transparente
            plot_bgcolor='#121420',   # Fondo de la gráfica transparente
            width=550,height=340,

            legend=dict(
        font=dict(size=12 )))
        fig.update_traces(marker_line_width=1.5, opacity=1)

        return fig




    def grafico_importancia(x_data,y_data,z_data,direccion,lado,empuje):
        colors = ['#79af61' if x > 0 else '#ca3013' for x in x_data]
        garfico_features = go.Figure(data=[
                go.Bar(name='Cumple', x=z_data.abs(), y=y_data, marker_color = colors,orientation='h' )])
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
            width=310,height=240,

            font=dict(
                family="Arimo ",   # Fuente del texto
                size=10,          # Tamaño del texto
                color="#FFFFFF"     # Color del texto
            ),
            barmode='group')
        return garfico_features

    def datos_humedad(prm,sdo,trc,cto,qto):
        consulta = f"""
                    SELECT TOP 4 
                    TS,
                    {prm},
                    {sdo},
                    {trc},
                    {cto},
                    {qto}
                FROM 
                    Lecturas_Resultados 
                ORDER BY 
                    TS DESC;
 
                    """
        data = load_data(consulta,'UBB')
        return data

    def datos_calidad(calidades):

        consulta = f"""
                    SELECT TOP 4 
                    TS,
                    {', '.join(calidades)}
                FROM 
                    Lecturas_Resultados 
                ORDER BY 
                    TS DESC;
 
                    """
        data = load_data(consulta,'UBB')
        data = trabajo(data)
        return data

    def trabajo(data):
        clear = ['A','B','BR','An','BPRs']
        ryc = ['No Info','Comp']
        data['Chapa clear'] = data[clear].sum(axis=1)
        data.drop(columns=clear, inplace=True)
        data['Random-Composer'] = data[ryc].sum(axis=1)
        data.drop(columns=ryc, inplace=True)
        print(data.columns)
        columns_to_exclude = ['Chapa clear', 'Random-Composer','TS']
        data['Otras calidades'] = data.drop(columns=columns_to_exclude).sum(axis=1)
        data.drop(columns=data.columns.difference(columns_to_exclude + ['Otras calidades']), inplace=True)
        return data



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
                    ORDER BY ROUND(s.Valor_Shap, 2) ASC;"""

        data = load_data(consulta,'Arauco')
        data = data.to_dict(orient='records')
        return data



    @app.callback(
    [Output('link-1', 'style'),
     Output('link-2', 'style'),
     Output('link-3', 'style')],
    [Input('navegador', 'pathname')]
    )

    def update_link_styles(pathname):
        # Estilos base para los enlaces
        base_style = {'fontSize': '20px', 'padding': '10px', 'textDecoration': 'none', 'color': 'black', 'margin': '0 20px'}
        selected_style = {'fontSize': '30px', 'padding': '10px', 'textDecoration': 'none', 'color': 'blue', 'margin': '0 20px'}
        
        link1_style = base_style
        link2_style = base_style
        link3_style = base_style

        # Update the selected link style
        if pathname == '/page-1':
            link1_style = selected_style
        elif pathname == '/page-2':
            link2_style = selected_style
        elif pathname == '/page-3':
            link3_style = selected_style

        return link1_style, link2_style, link3_style

    @app.callback(
        [
        Output('Estado_s24', 'style'),
        Output('Estado_s15', 'style'),
        Output('Estado_s18', 'style')],
        [Input('intervalo', 'n_intervals')])

    def update_graph(*args):
        consulta = f"""
            SELECT TOP 1 calidad_chapa_s24, calidad_chapa_s18, calidad_chapa_s15
            FROM Lecturas_Resultados
            ORDER BY TS DESC
        """
        Df = load_data(consulta, 'UBB')
        
        if not Df.empty:
            return [
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_s24'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_s15'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
                {"backgroundColor": "#79af61"} if Df['calidad_chapa_s18'].fillna('0').iloc[-1] == 'cumple' else {"backgroundColor": "#ca3013"},
            ]
        else:
            return {"backgroundColor": "#08AA49"} * 3




    @app.callback(
        [Output('alert_S24', 'value'),
        Output('alert_S18', 'value'),
        Output('alert_S15', 'value')],
        [Input('intervalo', 'n_intervals')])
    def update_graph(intervalo):
        consulta = f"""
            SELECT TOP 2 calidad_chapa_s24,calidad_chapa_s18,calidad_chapa_s15
            FROM Lecturas_Resultados
            order by TS DESC
            """
        Df = load_data(consulta,'UBB')
        s24 =  Df[Df['calidad_chapa_s24'].fillna('0') == 'No cumple'].shape[0] if not Df['calidad_chapa_s24'].isnull().all() else 0
        s18 =  Df[Df['calidad_chapa_s18'].fillna('0') == 'No cumple'].shape[0] if not Df['calidad_chapa_s18'].isnull().all() else 0
        s15 =  Df[Df['calidad_chapa_s15'].fillna('0') == 'No cumple'].shape[0] if not Df['calidad_chapa_s15'].isnull().all() else 0

        return[s24,s18,s15]



    @app.callback(
        [Output('Va_importantes', 'figure'),
        Output('tabla_rangos', 'data'),
        Output('Va_importantes_2', 'figure'),
        Output('gra_humedad_v1', 'figure'),
        Output('gra_calidades', 'figure')],
        #Output('Revisar_s24', 'n_clicks'),
        #Output('Revisar_s18', 'n_clicks'),
        #Output('Revisar_s15', 'n_clicks'),
        #Output('Revisar_chapa', 'n_clicks'),
        #Output('Revisar_clear', 'n_clicks')],


        [Input('Revisar_s24', 'n_clicks'),
        Input('Revisar_s18', 'n_clicks'),
        Input('Revisar_s15', 'n_clicks'),
        ],

        [State('alert_S24', 'value'),
         State('alert_S18', 'value'),
         State('alert_S15', 'value')])

    def update_graph(Revisar_S24,Revisar_S18,Revisar_S15,s24,s18,s15):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'Revisar_s18':
            consulta = f"""
                SELECT Variable_Shap,
                Valor_Shap
                FROM S18_Shap 
                order by ABS(Valor_Shap) asc
                """
            feature_tablero = load_data(consulta,'Arauco')
            if int(s18) > -10:
                total_positivo = feature_tablero[feature_tablero['Valor_Shap'] > 0]['Valor_Shap'].sum()
                total_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]['Valor_Shap'].sum()
                feature_tablero['porcentaje'] = feature_tablero.apply(calcular_porcentaje, axis=1,args=(total_positivo, total_negativo))
                dataset_positivo = feature_tablero[feature_tablero['Valor_Shap'] >= 0]
                dataset_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]

                garfico_positivo = grafico_importancia(dataset_positivo['Valor_Shap'],dataset_positivo['Variable_Shap'],dataset_positivo['porcentaje'],True,'right',f'% Empuje Positivo')
                garfico_negativo = grafico_importancia(dataset_negativo['Valor_Shap'],dataset_negativo['Variable_Shap'],dataset_negativo['porcentaje'],'reversed','left',f'% Empuje Negativo')
                datos = sharp('S18_Shap')

                list_humedades = ['Secador_18_AVG_HUMEDAD_6 AS [Menor 6%]','Secador_18_AVG_HUMEDAD_9_10 AS [Entre 6% - 8%]','Secador_18_AVG_HUMEDAD_9_10 AS [Entre 8% - 10%]','Secador_18_AVG_HUMEDAD_11_13 AS [Entre 10% - 13%]','Secador_18_AVG_HUMEDAD_14_100 AS [Mayor 14%]']
                lista_calidades = ['Calidad_TAG_Secador_18_VDA_A AS [A]' ,
                                    'Calidad_TAG_Secador_18_VDA_B AS [B]',
                                    'Calidad_TAG_Secador_18_VDA_BR AS [BR]',
                                    'Calidad_TAG_Secador_18_VDA_Bmn AS [Bmn]',
                                    'Calidad_TAG_Secador_18_VDA_High_Face AS [High Face]',
                                    'Calidad_TAG_Secador_18_VDA_Redry AS [Redry]',
                                    'Calidad_TAG_Secador_18_VDA_Refeed AS [Refeed]',
                                    'Calidad_TAG_Secador_18_VDA_Cext_H AS [Cext_H]',
                                    'Calidad_TAG_Secador_18_VDA_Cext AS [Cext]',
                                    'Calidad_TAG_Secador_18_VDA_An AS [An]',
                                    'Calidad_TAG_Secador_18_VDA_Cp AS [Cp]',
                                    'Calidad_TAG_Secador_18_VDA_BPRs AS [BPRs]',
                                    'Calidad_TAG_Secador_18_VDA_Cint AS [Cint]',
                                    'Calidad_TAG_Secador_18_VDA_D AS [D]',
                                    'Calidad_TAG_Secador_18_VDA_Comp AS [Comp]',
                                    'Calidad_TAG_Secador_18_VDA_Cp_H AS [Cp H]',
                                    'Calidad_TAG_Secador_18_VDA_Cint_GER AS [Cint GER]',
                                    'Calidad_TAG_Secador_18_VDA_D_GER AS [D GER]',
                                    'Calidad_TAG_Secador_18_VDA_ITA AS [ITA]',
                                    'Calidad_TAG_Secador_18_VDA_Cul AS [Cul]',
                                    'Calidad_TAG_Secador_18_VDA_C AS [C]',
                                    'Calidad_TAG_Secador_18_VDA_No_Info AS [No Info]']


                humedades = datos_humedad(*list_humedades)
                garfico_perfil = grafico_humedad_calidad(humedades,'Promedio Humedad Chapa Total')
                calidades = datos_calidad(lista_calidades)
                garfico_calidad = grafico_humedad_calidad(calidades,'Calidad Visual Chapa Total')

                return [garfico_negativo,datos,garfico_positivo,garfico_perfil,garfico_calidad]


        elif button_id == 'Revisar_s24' :
            consulta = f"""
                SELECT Variable_Shap,
                Valor_Shap
                FROM S24_Shap 
                order by ABS(Valor_Shap) asc
                """
            feature_tablero = load_data(consulta,'Arauco')
            if int(s24) >= 0:
                total_positivo = feature_tablero[feature_tablero['Valor_Shap'] > 0]['Valor_Shap'].sum()
                total_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]['Valor_Shap'].sum()
                feature_tablero['porcentaje'] = feature_tablero.apply(calcular_porcentaje, axis=1,args=(total_positivo, total_negativo))
                dataset_positivo = feature_tablero[feature_tablero['Valor_Shap'] >= 0]
                dataset_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]

                garfico_positivo = grafico_importancia(dataset_positivo['Valor_Shap'],dataset_positivo['Variable_Shap'],dataset_positivo['porcentaje'],True,'right',f'% Empuje Positivo')
                garfico_negativo = grafico_importancia(dataset_negativo['Valor_Shap'],dataset_negativo['Variable_Shap'],dataset_negativo['porcentaje'],'reversed','left',f'% Empuje Negativo')
                datos = sharp('S24_Shap')

                list_humedades = ['Secador_24_AVG_HUMEDAD_6 AS [Menor 6%]','Secador_24_AVG_HUMEDAD_7_8 AS [Entre 6% - 8%]','Secador_24_AVG_HUMEDAD_9_10 AS [Entre 8% - 10%]','Secador_24_AVG_HUMEDAD_11_13 AS [Entre 10% - 13%]','Secador_24_AVG_HUMEDAD_14_100 AS [Mayor 14%]']
                lista_calidades = ['Calidad_TAG_Secador_24_VDA_A AS [A]' ,
                                    'Calidad_TAG_Secador_24_VDA_B AS [B]',
                                    'Calidad_TAG_Secador_24_VDA_BR AS [BR]',
                                    'Calidad_TAG_Secador_24_VDA_Bmn AS [Bmn]',
                                    'Calidad_TAG_Secador_24_VDA_High_Face AS [High Face]',
                                    'Calidad_TAG_Secador_24_VDA_Redry AS [Redry]',
                                    'Calidad_TAG_Secador_24_VDA_Refeed AS [Refeed]',
                                    'Calidad_TAG_Secador_24_VDA_Cext_H AS [Cext_H]',
                                    'Calidad_TAG_Secador_24_VDA_Cext AS [Cext]',
                                    'Calidad_TAG_Secador_24_VDA_An AS [An]',
                                    'Calidad_TAG_Secador_24_VDA_Cp AS [Cp]',
                                    'Calidad_TAG_Secador_24_VDA_BPRs AS [BPRs]',
                                    'Calidad_TAG_Secador_24_VDA_Cint AS [Cint]',
                                    'Calidad_TAG_Secador_24_VDA_D AS [D]',
                                    'Calidad_TAG_Secador_24_VDA_Comp AS [Comp]',
                                    'Calidad_TAG_Secador_24_VDA_Cp_H AS [Cp H]',
                                    'Calidad_TAG_Secador_24_VDA_Cint_GER AS [Cint GER]',
                                    'Calidad_TAG_Secador_24_VDA_D_GER AS [D GER]',
                                    'Calidad_TAG_Secador_24_VDA_ITA AS [ITA]',
                                    'Calidad_TAG_Secador_24_VDA_Cul AS [Cul]',
                                    'Calidad_TAG_Secador_24_VDA_C AS [C]',
                                    'Calidad_TAG_Secador_24_VDA_No_Info AS [No Info]']


                humedades = datos_humedad(*list_humedades)
                garfico_perfil = grafico_humedad_calidad(humedades,'Promedio Humedad Chapa Total')
                calidades = datos_calidad(lista_calidades)
                garfico_calidad = grafico_humedad_calidad(calidades,'Calidad Visual Chapa Total')

                return [garfico_negativo,datos,garfico_positivo,garfico_perfil,garfico_calidad]


        elif button_id == 'Revisar_s15':
            consulta = f"""
                SELECT Variable_Shap,
                Valor_Shap
                FROM S15_Shap 
                order by ABS(Valor_Shap) asc
                """
            feature_tablero = load_data(consulta,'Arauco')
            if int(s15) >= 0:
                total_positivo = feature_tablero[feature_tablero['Valor_Shap'] > 0]['Valor_Shap'].sum()
                total_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]['Valor_Shap'].sum()
                feature_tablero['porcentaje'] = feature_tablero.apply(calcular_porcentaje, axis=1,args=(total_positivo, total_negativo))
                dataset_positivo = feature_tablero[feature_tablero['Valor_Shap'] >= 0]
                dataset_negativo = feature_tablero[feature_tablero['Valor_Shap'] < 0]

                garfico_positivo = grafico_importancia(dataset_positivo['Valor_Shap'],dataset_positivo['Variable_Shap'],dataset_positivo['porcentaje'],True,'right',f'% Empuje Positivo')
                garfico_negativo = grafico_importancia(dataset_negativo['Valor_Shap'],dataset_negativo['Variable_Shap'],dataset_negativo['porcentaje'],'reversed','left',f'% Empuje Negativo')
                datos = sharp('S15_Shap')
                
                list_humedades = ['Secador_15S_AVG_HUMEDAD_6 AS [Menor 6%]','Secador_15S_AVG_HUMEDAD_9_10 AS [Entre 6% - 8%]','Secador_15S_AVG_HUMEDAD_9_10 AS [Entre 8% - 10%]','Secador_15S_AVG_HUMEDAD_11_13 AS [Entre 10% - 13%]','Secador_15S_AVG_HUMEDAD_14_100 AS [Mayor 14%]']
                lista_calidades = ['Calidad_TAG_Secador_15_8ft_A AS [A]' ,
                                    'Calidad_TAG_Secador_15_8ft_B AS [B]',
                                    'Calidad_TAG_Secador_15_8ft_BR AS [BR]',
                                    'Calidad_TAG_Secador_15_8ft_Bmn AS [Bmn]',
                                    'Calidad_TAG_Secador_15_8ft_High_Face AS [High Face]',
                                    'Calidad_TAG_Secador_15_8ft_Redry AS [Redry]',
                                    'Calidad_TAG_Secador_15_8ft_Refeed AS [Refeed]',
                                    'Calidad_TAG_Secador_15_8ft_Cext_H AS [Cext_H]',
                                    'Calidad_TAG_Secador_15_8ft_Cext AS [Cext]',
                                    'Calidad_TAG_Secador_15_8ft_An AS [An]',
                                    'Calidad_TAG_Secador_15_8ft_Cp AS [Cp]',
                                    'Calidad_TAG_Secador_15_8ft_BPRs AS [BPRs]',
                                    'Calidad_TAG_Secador_15_8ft_Cint AS [Cint]',
                                    'Calidad_TAG_Secador_15_8ft_D AS [D]',
                                    'Calidad_TAG_Secador_15_8ft_Comp AS [Comp]',
                                    'Calidad_TAG_Secador_15_8ft_Cp_H AS [Cp H]',
                                    'Calidad_TAG_Secador_15_8ft_Cint_GER AS [Cint GER]',
                                    'Calidad_TAG_Secador_15_8ft_D_GER AS [D GER]',
                                    'Calidad_TAG_Secador_15_8ft_ITA AS [ITA]',
                                    'Calidad_TAG_Secador_15_8ft_Cul AS [Cul]',
                                    'Calidad_TAG_Secador_15_8ft_C AS [C]',
                                    'Calidad_TAG_Secador_15_8ft_No_Info AS [No Info]']


                humedades = datos_humedad(*list_humedades)
                garfico_perfil = grafico_humedad_calidad(humedades,'Promedio Humedad Chapa Total')
                calidades = datos_calidad(lista_calidades)
                garfico_calidad = grafico_humedad_calidad(calidades,'Calidad Visual Chapa Total')

                return [garfico_negativo,datos,garfico_positivo,garfico_perfil,garfico_calidad]  

        else:
            return dash.no_update


    @app.callback(
        Output("url2", "href"),
        [Input("id_revisar_panel", "n_clicks")],

        [State('Revisar_s24', 'n_clicks'),
        State('Revisar_s18', 'n_clicks'),
        State('Revisar_s15', 'n_clicks'),
        State('Revisar_chapa', 'n_clicks'),
        State('Revisar_clear', 'n_clicks')])


    def abrir_pagina(revisar,s24_count,s18_count,s15_count,chapa_count,clear_count):

        if not s18_count != None:
            s18_count = 0
        if not s24_count != None:
            s24_count = 0
        if not s15_count != None:
            s15_count = 0
        if not chapa_count != None:
            chapa_count = 0
        if not clear_count != None:
            clear_count = 0

        s18 = [s18_count,"https://lalagos.grafana.net/d/Varshap-040924_vs18/varshap-secador-s18?var-G1_Proceso=&var-G1_Maquina=&var-G1_Variable=&var-G1_Variable_UOM=&from=2024-08-31T14:19:42.270Z&to=2024-08-31T15:18:52.077Z&timezone=browser&kiosk="]
        s15 = [s15_count,"https://lalagos.grafana.net/d/Varshap-040924_vs15/varshap-secador-s15?kiosk=&from=2024-08-31T14:19:42.270Z&to=2024-08-31T15:18:52.077Z&timezone=browser"]
        s24 = [s24_count,"https://lalagos.grafana.net/d/Varshap-040924_vs24/varshap-secador-s24?from=2024-08-31T14:19:42.270Z&to=2024-08-31T15:18:52.077Z&timezone=browser&kiosk="]
        chapa = [chapa_count,"https://lalagos.grafana.net/d/Varshap-040924_v/variables?var-G1_Proceso=&var-G1_Maquina=&var-G1_Variable=&var-G1_Variable_UOM=&from=2024-08-31T14:19:42.270Z&to=2024-08-31T15:18:52.077Z&timezone=browser&kiosk="]
        clear = [clear_count,"https://lalagos.grafana.net/d/Varshap-040924_v/variables?var-G1_Proceso=&var-G1_Maquina=&var-G1_Variable=&var-G1_Variable_UOM=&from=2024-08-31T14:19:42.270Z&to=2024-08-31T15:18:52.077Z&timezone=browser&kiosk="]

        activar = {}
        activar['s18'] = s18
        activar['s15'] = s15
        activar['s24'] = s24
        activar['chapa'] = chapa
        activar['clear'] = clear

        if revisar != None:
            max_key = max(activar, key=lambda k: activar[k][0])
            max_url = activar[max_key][1]
            return max_url
       
        else:
            return dash.no_update


    @app.callback(
    [Output('titulo_variables', 'children'),
     Output('titulo_variables', 'style')],
    [Input('Revisar_s24', 'n_clicks'),
     Input('Revisar_s18', 'n_clicks'),
     Input('Revisar_s15', 'n_clicks')])
    def update_graph(Revisar_S24,Revisar_S18,Revisar_S15):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'Revisar_s18':
            return 'Importancia Variables S18',{'margin-left': 400}
        elif button_id == 'Revisar_s24':
            return 'Importancia Variables S24',{'margin-left': 400}
        elif button_id == 'Revisar_s15':
            return 'Importancia Variables S15',{'margin-left': 400}



        

       
        
