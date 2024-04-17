import pandas as pd
import matplot as plt

maps = ['de_inferno' 'de_nuke' 'de_mirage' 'de_dust2']



data = pd.read_csv('./db/dbcs.csv', engine='python', sep=';', encoding='utf-8')
matchs_id = data['MatchId'].unique() # 333 Games
count_maps = data['Map'].unique() # 4 Mapas

def count_map_per_game (matchs, maps):
    for m_id in matchs_id:
        pass
        
        
count_map_per_game(matchs, maps)