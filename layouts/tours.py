import requests

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from components.components import TourCard



def layout_list():
    tours = requests.get("http://127.0.0.1:5000/tours").json()["tours"]
    layout = html.Div([
    dbc.Row([
        dbc.Col([html.H1("Tours:")], width=12),
    ]),

    dbc.Row([
        dbc.Col([
            TourCard(x["tour_name"], x["tour_location"], x["num_stops"], x["tour_id"])
        ], width=3) for x in tours
    ])
    ])
    return layout


def layout_info(tour_id):
    # data = [item for item in tours if item["tour_id"] == int(tour_id)][0]
    data = requests.get("http://127.0.0.1:5000/tours/" + tour_id).json()
    layout = html.Div(
        html.H1(f"This is a test page for tour: {data['tour_name']}", className="display-2")
    )
    return layout