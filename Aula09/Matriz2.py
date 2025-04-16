matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo a matriz
print(matriz)

# Imprimir a segunda linha da matriz
print(matriz[1])

# Imprimir o caracter na posição linha, coluna (1, 2) na matriz
print(matriz[1][2])

# Desafio é percorrer a matriz mostrando todos os números em separado.
print('--- Solução do desafio ---')
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])