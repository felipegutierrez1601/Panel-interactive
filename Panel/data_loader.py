import pandas as pd

def load_data():
    mi_conexion = pyodbc.connect(
                Trusted_Connection='No',
                Authentication='ActiveDirectoryPassword',
                UID='',
                PWD= '',
                Driver='{SQL Server}',
                Server='',
                Database='')
    data = pd.read_sql('SELECT * FROM KPIS', mi_conexion)
    return data