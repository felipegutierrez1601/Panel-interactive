from dash import dcc
from datetime import date


def fecha(fecha_now,estilo):
        fecha = dcc.DatePickerSingle(
                id='Calendario',
                min_date_allowed=date(1995, 12, 12),
                max_date_allowed=date(2050, 12, 12),
                date = fecha_now,
                display_format='YYYY-MM-DD',
                classname = estilo
                )
        return fecha