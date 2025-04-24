from random import randint

q = []

for n in range(20):
    numero = randint(0, 1000)
    q.append(numero)

maior = -1
indice_maior = -1
menor = 1000
indice_menor = -1

for i in range(len(q)):
    # Teste se maior
    if q[i] > maior:
        maior = q[i]
        indice_maior = i
    # Teste se menor
    if q[i] < menor:
        menor = q[i]
        indice_menor = i

print(q)
print(f'O maior valor é {maior}.')
print(f'O índice do maior valor é {indice_maior}.')
print(f'O maior valor é {menor}.')
print(f'O índice do maior valor é {indice_menor}.')