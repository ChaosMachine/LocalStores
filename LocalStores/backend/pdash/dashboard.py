import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import dash_leaflet as dl
import dash_leaflet.express as dlx
from functions import get_location
from dash.dependencies import Input, Output, State
from flask import Flask
from test_db import User, db



# Generate some in-memory data.
<<<<<<< HEAD:backend/pdash/dashboard.py
Prague1 = dlx.dicts_to_geojson([dict(lat=50.064840, lon=14.442720), dict(lat=50.082525, lon=14.451692), dict(lat=50.075539, lon=14.437800)])
def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/dist/css/styles.css',
        ]
    )



    df_spending = pd.DataFrame({
=======




server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions']=True
# For Heroku deployment.

locations=[]
stores = User.query.all()
for store in stores:
    lon, lat = get_location(store.Location)
    locations.append(dict(lat=lat, lon=lon))
Prague1 = dlx.dicts_to_geojson(locations)


df_spending = pd.DataFrame({
>>>>>>> efa668cecbbd58fc41ada987376d984e03eb136b:index.py
    "Day": ["Mo", "Tue", "We", "Tu", "Fr", "Sa", "So"],
    "Amount": [300, 500, 0, 600, 200, 0, 400],
    })

    df_status = pd.DataFrame(
    {
        "Parameter": ["Points", "Level", "Number of visits"],
        "Value": ["5000", "3", "20"],
    }
    )

    df_ranking = pd.DataFrame(
    {
        "Place": [x for x in range(1,5)],
        "Username": ["chrisO", "DavidP", "JosefH", "PeterK"],
        "Level": ["5", "8", "20", "7"],
        "Points": ["5000", "8000", "20000", "7000"],
    }
    )


    fig_spending = px.bar(df_spending, x="Day", y="Amount", title="Purchases last week")
    fig_spending.update_layout({
    "plot_bgcolor": "rgba(0, 0, 0, 0)",
    "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })

regionalRanking = dbc.Table.from_dataframe(df_ranking, striped=True, bordered=True, hover=True)
friendsRanking = dbc.Table.from_dataframe(df_ranking, striped=True, bordered=True, hover=True)


<<<<<<< HEAD:backend/pdash/dashboard.py
    app.layout = html.Div([
=======
app.layout = html.Div([
    html.Div(id="lon"),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

dashboard = html.Div([
>>>>>>> efa668cecbbd58fc41ada987376d984e03eb136b:index.py

    dbc.Nav(
        [
            dbc.NavbarBrand(html.H3("Local Heroes"), className="ml-2"),
            dbc.NavLink("Dashboard", href="#"),
            dbc.NavLink("Sign-Up as Customer", href="/customerlogin"),
            dbc.NavLink("Sign-Up as Owner", href="/ownerlogin"),
            dbc.NavLink("Login", href="#"),
            dbc.NavLink("Invite Friends", href="#"),
        ], className= 'navbar navbar-expand-lg navbar-light bg-light fixed-top'
    ),
    # Row: Title
#    html.Div([
#        dbc.Input(id='inputLocation', type="text", className="col-4"),
#        dbc.Button("Get location", id="confirmLocation", color="primary", className="mr-1 mt-2"),
#        html.Div(id="lon"), html.Div(id="lat")
#    ], className="pt-5"),
    # Row: Map + Bar Chart

    html.Div([
        # Column: Map
        html.Div([
            html.H5("Map of local stores and restaurants"),
            dl.Map(center=[50.064840, 14.442720], zoom=13, children=[
                    dl.TileLayer(),
                    dl.GeoJSON(data=Prague1),
                # in-memory geojson (slowest option)
                ], style={'width': '100%', 'height': '35vh', 'margin': "auto", "display": "block"}, id="map"),
                html.Div(id="stores")
        ], className="col-md-4"),
        # Column: Bar Chart
        html.Div([
            html.H5("Statistics"),
            dbc.Table.from_dataframe(df_status, striped=True, bordered=True, hover=True)
        ], className="col-md-4"),
        html.Div([
            html.H5("Messages from store owners"),
            html.Article([
                html.Article([
                    html.P("Hey everone, today I am offering your a special thing bla bla bla")
                ],className="each_message2"),
            html.Article([
                    html.P("Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi,")
                ],className="each_message1"),
            html.Article([
                    html.P("At placeat explicabo temporibus eius est tenetur? Maiores impedit")
                ],className="each_message2"),
            html.Article([
                    html.P("Hello, we are open today until 10 pm. Stop by and try our new ...")
                ],className="each_message1")
            ],className="message_section")
        ], className="col-md-4")
    ], className="row my-5"),
    # Row: Line Chart + Donut Chart
    html.Div([
        # Column: Line Chart
        html.Div([
            html.H5("Rewards"),
            dbc.ListGroup([
                dbc.ListGroupItem("20% discount at Rob's Pizza"),
                dbc.ListGroupItem("Next beer for free at BeerGeek"),
                dbc.ListGroupItem("Free coffee at MyBackery"),
    ])], className="col-md-4"),
        html.Div([
            dcc.Graph(id="spending", figure=fig_spending)
        ], className="col-md-4"),
        html.Div([
            html.H5("Ranking"),
    dbc.Tabs(
        [
            dbc.Tab(regionalRanking, label="Friends"),
            dbc.Tab(friendsRanking, label="People Around Me")
        ]
    )
        ], className="col-md-4")
    ], className="row mt-5"),

    ], className="container-fluid pt-5")

<<<<<<< HEAD:backend/pdash/dashboard.py
    if __name__ == '__main__':
=======
customerlogin_layout = dbc.Container([
    dbc.FormGroup([
        dbc.InputGroup([
            dbc.Input(id="Username", placeholder="Username")],className="mt-5"),
dbc.InputGroup([
            dbc.Input(id="Password", placeholder="Password")],className="mt-2"),
        dbc.Button("Confirm_customer",id='Add_customer', color="primary", className="mr-1 mt-2"),

    ]),
    html.A("back to Dashboard",href="/")
], className="container login")


home_page_layout = dbc.Container([])

ownerlogin_layout = dbc.Container([
                        dbc.FormGroup([
                            dbc.InputGroup([
                                dbc.Input(id="nameOwner", placeholder="Name")],className="mt-5"),
                        dbc.InputGroup([
                                dbc.Input(id="locationOwner", placeholder="Location")],className="mt-2"),
                            dbc.Button("Confirm",id='Confirm_owner', color="primary", className="mr-1 mt-2")
                        ]),
                        html.A("back to Dashboard",href="/")
                    ], className="container login")


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/':
        return dashboard
    elif pathname == '/customerlogin':
        return customerlogin_layout
    elif pathname == '/ownerlogin':
        return ownerlogin_layout
    else:
        return '404'

#@app.callback(
#    Output('lon', 'children'),
#    [Input('Confirm_owner', 'n_clicks')],
#   [State('nameOwner','children'),
#     State('locationOwner','children')])

#def getCoordinates(n_clicks, name, location):
#   if n_clicks:
#        Owner = User(Name=name, Location=location)
#        db.session.add(Owner)
#        db.session.commit()
#    return


if __name__ == '__main__':
    app.run_server(debug=True)
>>>>>>> efa668cecbbd58fc41ada987376d984e03eb136b:index.py
