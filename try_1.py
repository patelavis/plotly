from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import json
import pandas as pd
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets = external_stylesheets)

styles = {
    'pre' : {
        'border' : 'thin lightgray solid',
        'overflowX' : 'scroll'
    }
}

df = pd.DataFrame({
    "x": [1,2,1,2],
    "y": [1,2,3,4],
    "customdata": [1,2,3,4],
    "fruit": ["apple", "apple", "orange", "orange"],
})

fig = px.scatter(df, x = 'x', y='y', color='fruit', custom_data=['customdata'])

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=20)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig,
    ),
    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
            ***Hower Data***
            Mouse over values in the graph.
            """),
            html.pre(id='hower-data', style=styles['pre'])
        ], className=)
    ])
])