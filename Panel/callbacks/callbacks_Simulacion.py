from dash.dependencies import Input, Output
from data_loader import load_data
import plotly.express as px

def register_callbacks_layout2(app):
    @app.callback(Output('Gra_simu', 'figure'),
                    Input('Gra_simu', 'id'))
    def update_figure(input_value):
        df = load_data()
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")