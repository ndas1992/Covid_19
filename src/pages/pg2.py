import plotly.express as px
from dash import Dash, Input, Output, dcc, html, callback
import pandas as pd
import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Vaccine Analysis')

df = pd.read_csv(r'INPUT/data/covid_vaccine_statewise.csv')
#print(df.head())
df_india = df[df['State'] == 'India']
df_other = df[df['State'] != 'India']


dropdown_1 = dcc.Dropdown(options=df['State'].unique(), id='state-choice1')
dropdown_2 = dcc.Dropdown(options=df.columns.values[2:], id='column-choice1')


layout = html.Div([
    dbc.Row([dbc.Col([dropdown_1], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4), dbc.Col([dropdown_2], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4)]),
    dbc.Row([dbc.Col([dcc.Graph(id='line-fig1', figure=px.line(df_other, x='Updated On', y='Total Doses Administered', color='State'))], width=12)])  
])

@callback(
    Output('line-fig1', 'figure'),
    Input('state-choice1', 'value'),
    Input('column-choice1', 'value')
)
def update_graph(state, column):
    if state is None and column is None:
        #print('1')
        #print(f'value = Naone')
        fig = px.line(df_other, x='Updated On', y='Total Doses Administered', color='State')
    elif state is None:
        #print('2')
        fig = px.line(df_other, x='Updated On', y=column, color='State')
    elif column is None:
        #print('3')
        dff = df[df['State'] == str(state)]
        fig = px.line(dff, x='Updated On', y='Total Doses Administered', color='State')
    if state and column:
        #print('4')
        dff = df[df['State'] == str(state)]
        fig = px.line(dff, x='Updated On', y=column, color='State')
    return fig