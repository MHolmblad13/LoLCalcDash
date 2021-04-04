import dash_bootstrap_components as dbc

def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
        dbc.NavItem(dbc.NavLink("LoLCalc", href='/pages/lolcalc')),
        dbc.NavItem(dbc.NavLink("LoLItems",href='/pages/lolitems'))
    ],
        brand="Calcs.gg",
        brand_href="/",
        sticky="top",
        color = "primary",
        dark = True
    )
    return navbar