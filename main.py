from dash import Dash, dcc, html
import dash
import dash_bootstrap_components as dbc


app = Dash(__name__, use_pages=True, pages_folder='src/pages', external_stylesheets=[dbc.themes.SPACELAB])
mytitle = dcc.Markdown(children='# Covid Data Analysis')
nav = dbc.Nav(
    [dbc.NavLink([html.Div(page['name'])], active='exact', href=page['path']) for page in dash.page_registry.values()],vertical=True, pills=True, class_name='bg-light'
)

app.layout = dbc.Container([
    
    dbc.Row([dbc.Col([mytitle],width=6)], justify='center'),
    
    html.Hr(),

    dbc.Row([dbc.Col([nav], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2), dbc.Col([dash.page_container], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)])

], fluid=True)


if __name__=="__main__":
    app.run_server(port=8051, debug=True)