from functions import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

matchs = findMatchs(data=data)
maps = ['de_inferno', 'de_nuke', 'de_mirage', 'de_dust2']

# T, CT
info_inferno = [0,0]
info_nuke = [0,0]
info_mirage = [0,0]
info_dust2 = [0,0]

# inferno1 = findMatch(4, data)
# inferno2 = findMatch(9, data)

# arr = [inferno1, inferno2]
# map string (int,int)

# for i in matchs:
#     matchs_obj = findWinnerOfMapByMatch(match=i)
#     if matchs_obj["Map"] == maps[0]:
#         info_inferno[0] += matchs_obj["Terrorist"]
#         info_inferno[1] += matchs_obj["CounterTerrorist"]
#     if matchs_obj["Map"] == maps[1]:
#         info_nuke[0] += matchs_obj["Terrorist"]
#         info_nuke[1] += matchs_obj["CounterTerrorist"]
#     if matchs_obj["Map"] == maps[2]:
#         info_mirage[0] += matchs_obj["Terrorist"]
#         info_mirage[1] += matchs_obj["CounterTerrorist"]
#     if matchs_obj["Map"] == maps[3]:
#         info_dust2[0] += matchs_obj["Terrorist"]
#         info_dust2[1] += matchs_obj["CounterTerrorist"]

map_info = {
    maps[0]: [0, 0],  # Inferno
    maps[1]: [0, 0],  # Nuke
    maps[2]: [0, 0],  # Mirage
    maps[3]: [0, 0]   # Dust2
}


for match in matchs:
    match_obj = findWinnerOfMapByMatch(match=match)
    map_name = match_obj["Map"]
    terrorist_score = match_obj["Terrorist"]
    counterterrorist_score = match_obj["CounterTerrorist"]
    
    # Actualizar la información del mapa correspondiente
    if map_name in map_info:
        map_info[map_name][0] += terrorist_score
        map_info[map_name][1] += counterterrorist_score

print(map_info)


# Extraer datos para graficar
T = [map_info[map_name][0] for map_name in maps]
CT = [map_info[map_name][1] for map_name in maps]
x = np.arange(len(maps))  # Índices para las barras

# Graficar
width = 0.35  # Ancho de las barras
fig, ax = plt.subplots()
barsT = ax.bar(x - width/2, T, width, label='T', color='orange')
barsCT = ax.bar(x + width/2, CT, width, label='CT', color='blue')

# Etiquetas y título
ax.set_xlabel('Mapas')
ax.set_ylabel('Número de victorias')
ax.set_title('Distribución de rondas ganadas por mapa y equipo')
ax.set_xticks(x)
ax.set_xticklabels(maps)
ax.legend()

# Mostrar gráfico
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visualización
plt.tight_layout() 
plt.savefig('bienwn.png')

