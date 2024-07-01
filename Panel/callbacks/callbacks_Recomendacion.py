from dash.dependencies import Input, Output
from data_loader import load_data
import plotly.express as px

def register_callbacks_layout1(app):
    @app.callback(Output('Grafico_reco', 'figure'),
                    Input('Grafico_reco', 'id'))
    def update_figure(input_value):
        df = load_data()
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
            
