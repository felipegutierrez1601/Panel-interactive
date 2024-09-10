import pyodbc
import joblib
import numpy as np
import pandas as pd

def normalizar(dataSet):
            with pyodbc.connect(
                    Trusted_Connection='No',
                    Authentication='ActiveDirectoryPassword',
                    UID='Felipe',
                    PWD='Fondef',
                    Driver='{SQL Server}',
                    Server='146.83.131.135',
                    Database='Arauco') as mi_conexion:
                escalado = pd.read_sql("SELECT * FROM escalar", mi_conexion)

                for column in dataSet.columns:
                    # Buscar los valores Xmin y Xmax de la variable actual
                    escalado_values = escalado[escalado['Variable'] == column]
                    if not escalado_values.empty:
                        Xmin = escalado_values['Xmin'].values[0]
                        Xmax = escalado_values['Xmax'].values[0]
                    
                        # Aplicar la normalización Min-Max
                        value = (dataSet[column] - Xmin)/(Xmax-Xmin)
                        value = value.iloc[0]
                        
                        if value < 0:
                            dataSet[column] = 0
                        elif value > 1:
                            dataSet[column] = 1
                        else:
                            dataSet[column] = value
                return dataSet



def simular(nameAlgoritmo, dataSet):
    dataSet_2 = normalizar(dataSet)
    print('ESTOOOOOOOO',dataSet_2)
    modelo_cargado = joblib.load(nameAlgoritmo)
    prediccion = modelo_cargado.predict(dataSet_2.values)
    return prediccion
    

def main(nameKpi, dataSet):
    if nameKpi == "rendimiento_clear":
        nameAlgoritmo = 'xgb_t_SGeneral_R_clear'
    elif nameKpi == "calidad_chapa_general":
        nameAlgoritmo = 'xgb_t_sGeneral_c_ch'
    elif nameKpi == "calidad_chapa_s15":
        nameAlgoritmo = 'xgb_t_s15_c_ch '
    elif nameKpi == "calidad_chapa_s18":
        nameAlgoritmo = 'xgb_t_s18_c_ch.pkl'
    elif nameKpi == "calidad_chapa_s24":
        nameAlgoritmo = 'xgb_t_s24_c_ch.pkl'

    simu = simular(nameAlgoritmo, dataSet)

    if simu[0] == 0:
         simu = 'No Cumple'
    else:
         simu = 'Cumple'
    
    return simu