import functions as f

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')

# print(f.FindMatchs(data))
halfs = f.findHalfsByMatch(data, 4)
# print(f.findRoundKillsByHalf(halfs))
print(f.findWinnersByHalf(halfs))

