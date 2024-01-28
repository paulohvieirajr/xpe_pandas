import pandas as pd

# Criação de uma série
s = pd.Series([1, 3, 5, 6, 8, 'ações', 'Stocks', 'ETFs'])
print('Exemplo de uma série contendo numeros e strings, sendo que a primeira coluna refere ao indice e a segunda aos dados: ')
print(s)

# Criação de um Dataframe
data = {'Acao' : ['Ambev', 'Wege', 'Vale'],
        'Preco': [15, 35, 68],
        'Dy': ['4%', '2%', '8%']}

df = pd.DataFrame(data)
print('Exemplo de um datafram, sendo que a primeira coluna refere ao indice e a segunda aos dados: ')
print(df)
