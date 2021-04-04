import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3("Welcome to Calcs.gg"),
                        html.P(
                            """ Test """
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)


def Homepage():
    layout = html.Div([
        body
    ])
    return layout