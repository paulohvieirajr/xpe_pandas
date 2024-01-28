import pandas as pd

# DataFrame com valores nulos aleatórios
data = {
    'Data': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04'],
    'Ação': ['AAPL', 'GOOG', None, 'MSFT'],
    'Preço': [150.5, None, 350.2, 280.7],
    'Volume': [1000000, 1500000, None, 800000],
    'Variação': [0.02, 0.01, 0.03, None]
}
df = pd.DataFrame(data)

# Exibindo o DataFrame original
print('DataFrame Original: \n')
print(df)

# Remoção de valores nulos
df_dropna = df.dropna() # Remove linhas com pelos menos um valor nulo.

# Preenchimento de valores nulos 
df_fillna = df.fillna(0) # Preenche valores nulos com 0
df_ffill = df.fillna(method='ffill') # Preenche os valores nulos com o último valor válido (preenchimento para frente)
df_bfill = df.fillna(method='bfill') # Preenche os valores nulos com o próximo valor válido  (preenchimento para trás)

# Varifica se existem valores nulos
df_isnull = df.isnull() # DataFrma booleano mostrando as células com valores nulos

# Varifica se existem valores nulos
df_notnull = df.notnull() # DataFrma booleano mostrando as células com valores nulos

# Exibindo resultados
print('\nDataFrame após a remoção de valores nulos: \n')
print(df_dropna)

print('\nDataFrame após o preenchimento de valores nulos: \n')
print(df_fillna)

print('\nDataFrame após o preenchimento para frente de valores nulos: \n')
print(df_ffill)

print('\nDataFrame após o preenchimento para trás de valores nulos: \n')
print(df_bfill)

print('\nDataFrame com verificação de valores nulos: \n')
print(df_isnull)

print('\nDataFrame com verificação de valores NÃO nulos: \n')
print(df_notnull)


