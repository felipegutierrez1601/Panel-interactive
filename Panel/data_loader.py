import pandas as pd

def load_data(consulta):
    mi_conexion = pyodbc.connect(
                Trusted_Connection='No',
                Authentication='ActiveDirectoryPassword',
                UID='Felipe',
                PWD= 'Fondef',
                Driver='{SQL Server}',
                Server='146.83.131.135',
                Database='UBB')
    data = pd.read_sql(consulta, mi_conexion)
    return data