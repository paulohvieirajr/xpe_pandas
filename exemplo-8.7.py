import pandas as pd

# Dicionário de dados 
data = {
    'coluna1': ['A', 'B', 'A', 'B', 'A'],
    'coluna2': [10, 20, 30, 45, 50]
}

df = pd.DataFrame(data)

# Agrupando e calculando media
grupo_media = df.groupby('coluna1').mean()

print('Media calculada com base no agrupamento: \n')
print(grupo_media)

# Agrupando e somando(sum)
grupo_sum = df.groupby('coluna1').sum()

print('\nSomatório calculado com base no agrupamento: \n')
print(grupo_sum)

data = {
    'coluna1': ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'coluna2': [10, 20, 10, 20, 30 ,30 , 30],
    'coluna3': [5, 15, 25, 35, 45, 55, 65]
}

df = pd.DataFrame(data)

grupo_media_combinada = df.groupby(['coluna1', 'coluna2']).mean()

print('\nMédia calculada com base no agrupamento combinado de 2 colunas: \n')
print(grupo_media_combinada)

