from dash import Dash, dcc, html, Input, Output, callback
from src.utils.misc import check
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash


dash.register_page(__name__, path='/', name='Home')

#data
df_stats = pd.read_csv(r'INPUT/data/covid_19_india.csv')

df_stats['State/UnionTerritory'] = df_stats['State/UnionTerritory'].apply(check)
#print(df_stats.head())
dropdown_1 = dcc.Dropdown(options=df_stats['State/UnionTerritory'].unique(), id='state-choice')
dropdown_2 = dcc.Dropdown(options=df_stats.columns.values[4:], id='column-choice')


layout = html.Div([
    dbc.Row([dbc.Col([dropdown_1], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4), dbc.Col([dropdown_2], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4)]),
    dbc.Row([dbc.Col([dcc.Graph(id='line-fig', figure=px.line(df_stats, x='Date', y='Cured', color='State/UnionTerritory'))], width=12)])  
])


@callback(
    Output('line-fig', 'figure'),
    Input('state-choice', 'value'),
    Input('column-choice', 'value')
)
def update_graph(state, column):
    
    if state is None and column is None:
        #print('1')
        #print(f'value = Naone')
        fig = px.line(df_stats, x='Date', y='Cured', color='State/UnionTerritory')
    elif state is None:
        #print('2')
        fig = px.line(df_stats, x='Date', y=column, color='State/UnionTerritory')
    elif column is None:
        #print('3')
        dff = df_stats[df_stats['State/UnionTerritory'] == str(state)]
        fig = px.line(dff, x='Date', y='Cured', color='State/UnionTerritory')
    if state and column:
        #print('4')
        dff = df_stats[df_stats['State/UnionTerritory'] == str(state)]
        fig = px.line(dff, x='Date', y=column, color='State/UnionTerritory')
    return fig