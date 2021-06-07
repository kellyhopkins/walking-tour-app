import dash_bootstrap_components as dbc
import dash_html_components as html

def TourCard(title, location, stops, tour_id):
    card = dbc.Card(dbc.CardBody([
        html.H5(f"{title}", className="card-title"),
        html.P(f"Location: {location}"),
        html.P(f"Number of Stops: {stops}"),
        html.P("test", className="d-none"),
        dbc.Button("Go somewhere", color="primary", href=f"/tours/{tour_id}"),
    ]))

    return card