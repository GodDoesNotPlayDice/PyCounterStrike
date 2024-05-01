import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

# Seleccionar las columnas 'MatchId' y 'Map'
matchs_maps = data[['MatchId', 'Map']]

# Eliminar filas duplicadas para obtener una fila por cada combinación única de 'MatchId' y 'Map'
unique_matchs_maps = matchs_maps.drop_duplicates()

# Contar cuántas veces aparece cada mapa en el conjunto de datos
map_counts = unique_matchs_maps['Map'].value_counts().reset_index()
map_counts.columns = ['Map', 'Total_Played']

# Identificar el mapa con el mayor número de kills
map_with_most_kills = map_counts.loc[map_counts['Total_Played'].idxmax()]
print("Mapa con más kills:", map_with_most_kills['Map'], "Total de partidas jugadas:", map_with_most_kills['Total_Played'])
