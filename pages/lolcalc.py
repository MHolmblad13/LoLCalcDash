#Layout page for the calculator
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Label import Label
from dash.dependencies import Input, Output
import pandas as pd

# Backend files
from app import app
from Heimer import champions, items

champArray = [{'label':name, 'value':name} for name in champions.champList]

layout = html.Div(
    [
        dbc.Row([
            dbc.Col( html.Div([
                dcc.Dropdown( #apparently there is an optimization here
                    id='champ1',
                    options=[{'label':name, 'value':name} for name in champions.champList],
                    value='Aatrox',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1level',
                    options=[
                        {'label':num, 'value':num} for num in range(1, 19)
                    ],
                    value=1,
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1item1',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1item2',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1item3',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1item4',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1item5',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ1item6',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                ]
                ),
            ),
            dbc.Col( html.Div([
                dcc.Dropdown(
                    id='champ2',
                    options=[
                        {'label':name, 'value':name} for name in champions.champList
                    ],
                    value='Aatrox',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2level',
                    options=[
                        {'label':num, 'value':num} for num in range(1, 19)
                    ],
                    value=1,
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2item1',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2item2',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2item3',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2item4',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2item5',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                dcc.Dropdown(
                    id='champ2item6',
                    options=[
                        {'label':name, 'value':name} for name in items.itemNames
                    ],
                    value='Boots',
                    className='w-25'
                ),
                ]
                ),
            ),
        ]),
        html.Div(id='test'),
        html.Div(id='test2'),
        html.Div(id='test3'),
        html.Div(id='test4'),
        html.Div(id='test5'),
        html.Div(id='test6'),
    ]
)

# champ 1 name
@app.callback(
    Output('test','children'),
    [Input('champ1','value')]
)
def champ1NameData(champ1):
    return 'You have selected "{}"'.format(champ1)

@app.callback(
    Output('test2','children'),
    [Input('champ1level','value')]
)
def champ1LevelData(champ1level):
    return 'You have selected "{}"'.format(champ1level)

@app.callback(
    Output('test3','children'),
    [
        Input('champ1item1', 'value'),
        Input('champ1item2', 'value'),
        Input('champ1item3', 'value'),
        Input('champ1item4', 'value'),
        Input('champ1item5', 'value'),
        Input('champ1item6', 'value')
    ]
)
def champ1ItemData(champ1item1,champ1item2, champ1item3, champ1item4, champ1item5, champ1item6):
    return "Hi"

# champ 2 data
@app.callback(
    Output('test4','children'),
    [Input('champ2','value')]
)
def champ2NameData(champ2):
    return 'You have selected "{}"'.format(champ2)

@app.callback(
    Output('test5','children'),
    [Input('champ2level','value')]
)
def champ2LevelData(champ2level):
    return 'You have selected "{}"'.format(champ2level)

@app.callback(
    Output('test6','children'),
    [
        Input('champ2item1', 'value'),
        Input('champ2item2', 'value'),
        Input('champ2item3', 'value'),
        Input('champ2item4', 'value'),
        Input('champ2item5', 'value'),
        Input('champ2item6', 'value')
    ]
)
def champ2ItemData(champ2item1,champ2item2, champ2item3, champ2item4, champ2item5, champ2item6):
    return "Hi"