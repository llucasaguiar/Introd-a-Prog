# Desenvolva um programa que verifique e mostre os
# números entre 1.000 e 2.000 que,
# quando divididos por 11, produzam o resto igual a 5.

numero = 1000

while numero <= 2000:
    if numero % 11 == 5:
        print(f'O número é {numero}.')

    # munero = numero + 1
    numero += 1