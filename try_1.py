from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd
import numpy as np

df = pd.read_csv('')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id = "graph-with-slider"),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])

@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    fig = px.scatter(filtered_df, x =
