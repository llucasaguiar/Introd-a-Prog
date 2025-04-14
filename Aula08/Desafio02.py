# Refaça o exercício da tabuada:

# Faça um programa que receba um número e que calcule a tabuada desse número."

# Mas, agora salve o resultado em um arquivo de texto.
numero = float(input('Digite o número desejado: '))
nome_arquivo = 'Desafio02.txt'

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:

    for m in range(1, 11):
        resultado = numero * m
        arquivo.write(f'{numero} * {m} = {resultado}\n')

print('--- Programa concluído! ---')
