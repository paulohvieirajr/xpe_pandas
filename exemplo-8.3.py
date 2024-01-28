import pandas as pd

# Importação de dados de um arquivo CSV.
df = pd.read_csv('./california_housing_test.csv')

print('Exemplo de uso de head: pega 5 primeiras linhas. \n')
print(df.head())

print('\nExemplo de uso de tail: pega 5 ultimas linhas. \n')
print(df.tail())

print('\nExemplo de uso de sample: pega 1 linha aleatória. \n')
print(df.sample())

print('\nExemplo de uso de info: traz dados sobre o dataframe. \n')
print(df.info())

print('\nOferece informações descritivas sobre as colunas do dataframe: media, desvio padrão, porcentagens.  \n')
print(df.describe())
