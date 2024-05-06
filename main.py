from functions import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

# Estudiar la duración de vida de los dos bandos por ronda para entender cómo influye en el resultado de la ronda
# match = findMatch(data=data, match_id=13)
dust2 = 'de_dust2'

matchs = findMatchsByMap(data, dust2)
dust2K = [sum(i['RoundKills']) for i in matchs]

t_arr = []
ct_arr = []
for i in matchs:
    rndkills = findRoundKillsByTeamByMatch(i)
    t_arr.append(sum(rndkills[0]))
    ct_arr.append(sum(rndkills[1]))

# Convertir a numpy array si no lo es
dust2K = np.array(dust2K)
t_arr = np.array(t_arr)
ct_arr = np.array(ct_arr)

# Calcular el coeficiente de correlación de Pearson
corr_T, _ = pearsonr(t_arr, dust2K)
corr_CT, _ = pearsonr(ct_arr, dust2K)

# Calcular la línea de correlación de Pearson para T-side
slope_T = corr_T * (np.std(t_arr) / np.std(dust2K))
intercept_T = np.mean(t_arr) - (slope_T * np.mean(dust2K))

# Calcular la línea de correlación de Pearson para CT-side
slope_CT = corr_CT * (np.std(ct_arr) / np.std(dust2K))
intercept_CT = np.mean(ct_arr) - (slope_CT * np.mean(dust2K))

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))

# Graficar T-side
plt.scatter(dust2K, t_arr, color='red', label='T-side')
plt.plot(dust2K, slope_T*dust2K + intercept_T, color='red', linestyle='--', label=f'Corr Line T-side {corr_T:.2f}')

# Graficar CT-side
plt.scatter(dust2K, ct_arr, color='blue', label='CT-side')
plt.plot(dust2K, slope_CT*dust2K + intercept_CT, color='blue', linestyle='--', label=f'Corr Line CT-side {corr_CT:.2f}')

plt.title('Gráfico de dispersión de kills por ronda de los equipos en de_dust2')
plt.xlabel('Total de kills por ronda')
plt.ylabel('Total de kills por equipo')
plt.legend()
plt.grid(True)
plt.show()
