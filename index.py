# -*- coding: utf-8 -*-

# Home Page for the site

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Label import Label
from dash.dependencies import Input, Output
import plotly.express as px

from common_comp import navbar

#pages
from app import app
from pages import lolcalc
from common_comp import home

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar.Navbar(),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/lolcalc':
        return lolcalc.layout
    #elif pathname == '/contact':
    #    return contact.contactPage()
    else:
        return home.Homepage()

server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)