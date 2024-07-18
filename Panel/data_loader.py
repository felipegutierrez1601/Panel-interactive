import pandas as pd

def load_data():
    mi_conexion = pyodbc.connect(
                Trusted_Connection='No',
                Authentication='ActiveDirectoryPassword',
                UID='Felipe',
                PWD= 'Fondef',
                Driver='{SQL Server}',
                Server='146.83.131.135',
                Database='Arauco')
    data = pd.read_sql('SELECT * FROM KPIS', mi_conexion)
    return data