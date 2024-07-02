from datetime import datetime

def get_fecha():
    # Obtener la fecha y hora actuales
    now = datetime.now()
    # Formatear la fecha y hora como una cadena
    fecha_formateada = now.strftime("%Y-%m-%d")
    return fecha_formateada


