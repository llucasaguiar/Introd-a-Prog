filmes = [
    'Sobreviventes',
    'Pulp Fiction',
    'Up',
    'Sherek',
    'O lobo de wall street',
    'Star Trek'
]

# Imprimir a lista completa
# type indica que foi empregada uma lista
print(type(filmes))

print(filmes)
print('-------------')

# upper serve para deixar em caixa alta
print(filmes[1].upper())

# Percorrer a lista de filmes
print('--- Percorrendo uma lista (fácil) ---')
for filme in filmes:
    print(filme.upper())

# Percorrer a lista - Vetor
# len função que calcula o tamanho das coisas. Ex.: tamanho de uma lista.
print('--- Percorrer a lista - Vetor ---')
for i in range(len(filmes)):
    print(filmes[i])
