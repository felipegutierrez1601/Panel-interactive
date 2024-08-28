from dash import html, dcc
import plotly.express as px
from data_loader import load_data
"""
def create_layout(app):
    df = load_data()
    dcc.Interval(id = 'intervalo', interval = 1000)
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    return html.Div(children=[
        html.H1(children='Dashboard Simulacion'),

        dcc.Link('Recomendacion', href='/Recomendacion'),
        html.Br(),
        dcc.Link('Refuerzo', href='/Refuerzo'),

        dcc.Graph(
            id='Gra_simu',
            figure=fig
        )
    ])
"""

def create_layout(app):

    simulacion = html.Div([

        html.Div([
                    dcc.Location(id='navegador',refresh=False),
                    html.Div([
                        dcc.Link(
                            [
                                html.Img(src='/assets/home_2.png'),  # Imagen como icono
                            ],
                            href='/Principal',className='icon-link'),
                        html.Div(dcc.Link('Recomendación', href='/Recomendacion',id='link-2'),className='link',style={'margin-left':249}),
                        html.Div(dcc.Link('Refuerzo', href='/Refuerzo',id='link-1'),className ='link2'),
                        html.Div(dcc.Link('Simulación', href='Simulacion',id='link-3'),style= {'margin-left' : 453,'margin-top':'2px','font-family': 'Scene', 'padding': '2px' '5px','background-color': '#FFFFFF','border-radius': '15px','border': '2px solid #000000','width':'150px','font-size': '1px','height': '37px'}),
                    ], id='link-container', className='link-container')
                ]),
                        ],style = {'background': '#FFFFFF','height': '100vh','posicion': 'absolute'})

    return simulacion