from functions import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
db = 'https://raw.githubusercontent.com/razbackup/CSV-EV2/main/dbcs.csv'
data = pd.read_csv(db, engine='python', sep=';', encoding='utf-8')



print(findWinnerByMap(4, data))
