import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

HeaderMain = dbc.Row([
        dbc.Col(html.Div([
            dbc.Jumbotron([
                html.H1("Walking Tour App", className="display-4"),
                html.Hr(className='my-2'),
                html.P("About the Project")
            ])
        ], style={"color": "black"}))
    ])