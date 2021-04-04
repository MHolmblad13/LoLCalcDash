import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CERULEAN,'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,#)
                suppress_callback_exceptions=True)
server = app.server

suppress_callback_exceptions=True