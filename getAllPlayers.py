from nba_api.stats.static import players
import pandas as pd

def getAllPlayers():
    players_full_name = []
    all_players = pd.DataFrame(players.get_players())
    for ind in all_players.index:
        if(all_players["is_active"][ind] == True):
            players_full_name.append(all_players["full_name"][ind])
    return players_full_name

def findPlayerId(full_name):
    all_players = pd.DataFrame(players.get_active_players())
    for i in all_players.index:
        if(all_players['full_name'][i] == full_name):
            player_id = all_players['id'][i]
    return player_id

