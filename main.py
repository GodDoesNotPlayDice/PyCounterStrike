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
match = findMatch(data=data, match_id=4)
dust2 = 'de_dust2'

# Econtrar el match de dust2
m = findMatchsByMap(data, dust2)

# Time and Distance (X , Y)
dust2_map = [findTimeAliveByTeamByMatch(m), findTravelledDistanceByTeamByMatch(m)]

# Calcular el coeficiente de correlación de Pearson para Terroristas y Contra-Terroristas en de_dust2
pearson_corr_T, _ = pearsonr(dust2_map[0][0], dust2_map[1][0])
pearson_corr_CT, _ = pearsonr(dust2_map[0][1], dust2_map[1][1])

# Graficar el gráfico de correlación de Pearson
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Para Terroristas
sns.regplot(x=dust2_map[0][0], y=dust2_map[1][0], ax=axs[0], color='red', scatter_kws={'alpha':0.4})
axs[0].set_title(f'de_dust2 - Terroristas\nPearson correlación: {pearson_corr_T:.2f}')
axs[0].set_xlabel('Tiempo en vida (segundos)')
axs[0].set_ylabel('Distancia recorrida (metros)')

# Para Contra-Terroristas
sns.regplot(x=dust2_map[0][1], y=dust2_map[1][1], ax=axs[1], color='blue', scatter_kws={'alpha':0.4})
axs[1].set_title(f'de_dust2 - Contra-Terroristas\nPearson correlación: {pearson_corr_CT:.2f}')
axs[1].set_xlabel('Tiempo en vida (segundos)')
axs[1].set_ylabel('Distancia recorrida (metros)')

plt.tight_layout()
plt.show()
