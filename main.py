from dash import Dash, html, dcc, Input, Output, callback
from getTeamStats import handleScrapping
from getAllPlayers import getAllPlayers, findPlayerId
import dash_bootstrap_components as dbc

app = Dash(__name__)
players = getAllPlayers()
app.layout = dbc.Container([
    dbc.Row([
        html.Div('NBA Bets Analysis Panel', className="text-primary text-center fs-3")
    ]),
    dbc.Row([
      dcc.Dropdown(players,'Kevin Durant', id='players-dropdown')
    ]),
    dbc.Row([
        html.Div('', id='output')
    ])
],fluid =True)

@callback(
    Output('output', 'children'),
    Input('players-dropdown', 'value')
)
def update_output(value):
    p_id = findPlayerId(value)
    return f'You have selected {p_id}'

if __name__ == '__main__':
    app.run(debug=True)