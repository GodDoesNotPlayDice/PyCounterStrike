import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

matchs_maps = data[['MatchId', 'Map']] # Saco solo las columnas MatchId y Map 79157 rows
unique_matchs_maps = matchs_maps.drop_duplicates() # Filtra los IDS dejandolos unicos 333 rows
map_counts = unique_matchs_maps['Map'].value_counts().reset_index() # Cuenta por ID unico de Mapas un tipo de grupo de 4 y cuenta cuantas veces cae el ID en relacion al mapa
print(map_counts)
map_counts.columns = ['Map', 'Total_Played']

plt.figure(figsize=(10, 6))
plt.bar(map_counts['Map'], map_counts['Total_Played'], color='skyblue')

# Añade etiquetas y título
plt.xlabel('Map')
plt.ylabel('Total Played')
plt.title('Total Played per Map')

# Rota las etiquetas del eje x para mayor legibilidad
plt.xticks(rotation=90)

# guardar la imagen en un archivo
plt.show()