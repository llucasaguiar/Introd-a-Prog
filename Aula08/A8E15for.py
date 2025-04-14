# Faça um programa que receba um número
# e que calcule a tabuada desse número.

numero = float(input('Digite um númeor: '))

for m in range(1, 11):
    resultado = numero * m
    print(f'{numero} x {m} = {resultado}')
