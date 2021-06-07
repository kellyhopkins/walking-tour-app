import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import requests

from components.components import TourCard
from components.headers import HeaderMain
from layouts import tours


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

container = html.Div([
    dcc.Location(id='url', refresh=False),
    HeaderMain,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    routes = {
        "/": tours.layout_list(),
    }
    print(pathname)
    if pathname in routes:
        return routes[pathname]
    else:
        if pathname.startswith("/tours/"):
            tour_id = pathname.split("/")[-1]
            return tours.layout_info(tour_id)

app.layout = dbc.Container(container, fluid=True)

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)