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
stanPointsList = [0,1,2,3,4,5] # this is for all abilities and udyr
rStanPointsList = [0,1,2,3] # standard amount of R points
rShapeList = [0,1,2,3,4] # this is for jayce, nidalee, elise

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
                dbc.Row([
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                Q
                            '''),
                            dcc.Dropdown(
                                id='champ1Q',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]),  
                        width = 2   
                    ),
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                W
                            '''),
                            dcc.Dropdown(
                                id='champ1W',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]),    
                        width = 2   
                    ),
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                E
                            '''),
                            dcc.Dropdown(
                                id='champ1E',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]),
                        width = 2    
                    ),
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                R
                            '''),
                            dcc.Dropdown(
                                id='champ1R',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]), 
                        width = 2
                    ),
                ])
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
                dbc.Row([
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                Q
                            '''),
                            dcc.Dropdown(
                                id='champ2Q',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]),  
                        width = 2   
                    ),
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                W
                            '''),
                            dcc.Dropdown(
                                id='champ2W',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]),    
                        width = 2   
                    ),
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                E
                            '''),
                            dcc.Dropdown(
                                id='champ2E',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]),
                        width = 2    
                    ),
                    dbc.Col(
                        html.Div([
                            dcc.Markdown('''
                                R
                            '''),
                            dcc.Dropdown(
                                id='champ2R',
                                options=[
                                    {'label':point, 'value':point} for point in stanPointsList
                                ],
                                value='0',
                                className='w-75'
                            ),
                        ]), 
                        width = 2
                    ),
                ])
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
    [Input('champ1','value'),
    Input('champ1level','value'),
    Input('champ1item1', 'value'),
    Input('champ1item2', 'value'),
    Input('champ1item3', 'value'),
    Input('champ1item4', 'value'),
    Input('champ1item5', 'value'),
    Input('champ1item6', 'value'),
    Input('champ1Q','value'),
    Input('champ1W', 'value'),
    Input('champ1E', 'value'),
    Input('champ1R', 'value')]
)
def champ1NameData(champ1, champ1level, champ1item1, champ1item2, champ1item3, champ1item4, champ1item5, champ1item6,
                    champ1Q, champ1W, champ1E, champ1R):
    calcStats = champions.GetChampionInfo(champ1, champ1level)
    itemStats1 = items.getFlatBaseStats(champ1item1)
    itemStats2 = items.getFlatBaseStats(champ1item2)
    itemStats3 = items.getFlatBaseStats(champ1item3)
    itemStats4 = items.getFlatBaseStats(champ1item4)
    itemStats5 = items.getFlatBaseStats(champ1item5)
    itemStats6 = items.getFlatBaseStats(champ1item6)
    # next add in mythic passives
    # then add item passive stats
    # then figure out a way to add item bonus effects like shock
    # then add ability passive stats
    # then add trigger for steroid stats
    return 'You have selected "{}", with stats {}'.format(champ1, calcStats)