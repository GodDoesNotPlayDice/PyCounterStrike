import functions as f
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

# Encontrar los datos de Terrorist y CounterTerrorist para cada mitad
matchs = f.findMatchs(data)
T_arr_half1 = []
CT_arr_half1 = []
T_arr_half2 = []
CT_arr_half2 = []

for match in matchs:
    halfs = f.findHalfsByMatch(data, match)
    half_one, half_two = f.findWinnersByHalf(halfs)
    T_arr_half1.append(half_one['Terrorist'])
    CT_arr_half1.append(half_one['CounterTerrorist'])
    T_arr_half2.append(half_two['Terrorist'])
    CT_arr_half2.append(half_two['CounterTerrorist'])

# Agrupar los datos en intervalos de 10 partidas y calcular el promedio
def group_and_average(data):
    grouped_data = []
    for i in range(0, len(data), 10):
        group = data[i:i+10]
        avg = sum(group) / len(group)
        grouped_data.append(avg)
    return grouped_data

T_arr_half1_grouped = group_and_average(T_arr_half1)
CT_arr_half1_grouped = group_and_average(CT_arr_half1)
T_arr_half2_grouped = group_and_average(T_arr_half2)
CT_arr_half2_grouped = group_and_average(CT_arr_half2)

# Crear los gráficos
plt.figure(figsize=(12, 6))

# Primer gráfico para la primera mitad
plt.subplot(1, 2, 1)
plt.plot(range(0, len(T_arr_half1_grouped) * 10, 10), T_arr_half1_grouped, label='Terrorist')
plt.plot(range(0, len(CT_arr_half1_grouped) * 10, 10), CT_arr_half1_grouped, label='CounterTerrorist')
plt.xlabel('Partidos')
plt.ylabel('Promedio de Rondas Ganadas')
plt.title('Primera Mitad (Cada 10 partidos)')
plt.legend()

# Segundo gráfico para la segunda mitad
plt.subplot(1, 2, 2)
plt.plot(range(0, len(T_arr_half2_grouped) * 10, 10), T_arr_half2_grouped, label='Terrorist')
plt.plot(range(0, len(CT_arr_half2_grouped) * 10, 10), CT_arr_half2_grouped, label='CounterTerrorist')
plt.xlabel('Partidos')
plt.ylabel('Promedio de Rondas Ganadas')
plt.title('Segunda Mitad (Cada 10 partidos)')
plt.legend()

# Ajustar el espacio entre los gráficos
plt.tight_layout()

# Mostrar los gráficos
plt.show()
