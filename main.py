import pandas as pd
import matplot as plt

data = pd.read_csv('./db/dbcs.csv', engine='python', sep=';', encoding='utf-8')
matchs = data['MatchId'].unique()
print(matchs) # 333 Partidas

# corr_matrix = data.corr(data)
# plt.figure(figsize=(12, 8))
# plt.title('Correlação entre as variáveis')
# plt.show()