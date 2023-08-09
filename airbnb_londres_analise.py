# %%
#Informações

#Este dataset contém dados de imóveis listados na plataforma AirBnb da cidade de Londres - UK no ano de 2022.

# %%
#Importando as bibliotecas

import pandas as pd
import seaborn as sns

# %%
#Carregando o dataset

df = pd.read_csv('./dataset/airbnb-londres2022.csv')
df

# %%

#Analisando informações gerais sobre o dataframe

df.head
df.describe

# %%
