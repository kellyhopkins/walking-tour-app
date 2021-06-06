import requests

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from components.components import TourCard

tours = requests.get("http://127.0.0.1:5000/tours").json()["tours"]

layout = html.Div([
    dbc.Row([
        dbc.Col([html.H1("Tours:")], width=12),
    ]),

    dbc.Row([
        dbc.Col([
            TourCard(x["tour_name"], x["tour_location"], x["num_stops"]) #for x in tours
        ], width=3) for x in tours
    ])
])