from functions import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
# import seaborn as sns

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

# match = findMatch(data=data, match_id=13)
maps = {
    'de_mirage': [],
    'de_inferno': [],
    'de_nuke': []
}
killsbyteam = {
    'de_mirage' : [],
    'de_inferno': [],
    'de_nuke': []
}

for i in maps:
    maps[i] = findMatchByMap(data, i)
    killsbyteam[i] = findRoundKillsByTeamByMatch(maps[i])
    

killsbyteam['de_mirage'] = [sum(killsbyteam['de_mirage'][0]), sum(killsbyteam['de_mirage'][1])]

killsbyteam['de_inferno'] = [sum(killsbyteam['de_inferno'][0]), sum(killsbyteam['de_inferno'][1])]

killsbyteam['de_nuke'] = [sum(killsbyteam['de_nuke'][0]), sum(killsbyteam['de_nuke'][1])]


# Crear las barras para cada mapa
for mapa, kills in killsbyteam.items():
    plt.figure(figsize=(8, 6))
    plt.bar(['T', 'CT'], kills, color=['blue', 'orange'])
    plt.xlabel('Equipo')
    plt.ylabel('Kills')
    plt.title('Kills por equipo en ' + mapa)
    #img
    plt.savefig(f'xd {mapa}.png')
    plt.show()