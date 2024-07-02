from .Funciones import fecha
from .constantes import get_fecha

def widget_fecha(estilo):
	Date_calendar = fecha(get_fecha(),estilo)
	return Date_calendar