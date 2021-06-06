import dash_bootstrap_components as dbc
import dash_html_components as html

def TourCard(title, location, stops):
    card = dbc.Card(dbc.CardBody([
        html.H5(f"{title}", className="card-title"),
        html.P(f"Location: {location}"),
        html.P(f"Number of Stops: {stops}"),
        dbc.Button("Go somewhere", color="primary"),
    ]))

    return card