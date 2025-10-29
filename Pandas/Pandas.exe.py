import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

df = pd.read_csv ('planilha.csv', )
print (df[['PRODUTO', 'PRECO', 'ESTOQUE']])

sns.set(style='whitegrid')  # Estilo limpo com grade
sns.set_palette('pastel')   # Paleta de cores suave

sns.barplot(x='PRODUTO', y='ESTOQUE', data=df)
plt.title('Estoque por produto', fontsize=20)
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()

conn = sqlite3.connect('meubanco.db')

df.to_sql('planilha', conn, index= False, if_exists='replace')

