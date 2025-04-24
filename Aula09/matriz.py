from random import randint

matriz = []

for i in range(5):
    lista_temporaria = []

    for j in range(5):
        lista_temporaria.append(randint(0, 1000))

    matriz.append(lista_temporaria)

# Percorrer a matriz utilizando o conceito de vetores e matriz

for linha in range(len(matriz)):
    print(matriz[linha])
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])

maior = -1

for linha in range(len(matriz)):

    for coluna in range(len(matriz[linha])):
        if maior < matriz[linha][coluna]:
            maior = matriz[linha][coluna]

print(f'O maior valor é: {maior}.')
print(matriz)