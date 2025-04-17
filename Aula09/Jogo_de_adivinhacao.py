# Implemente um jogo onde o computador escolhe
# um número aleatório entre 1 e 100, e o usuário tenta
# adivinhar. Utilize um loop para permitir que o usuário
# faça várias tentativas, fornecendo dicas (maior ou menor)
# a cada tentativa.

from random import randint

numero = randint(1, 100)
tentativas = int(input('Escolha quantas tentativas: '))

for i in range(tentativas):
    palpite = int(input('Qual o seu palpite: '))

    if numero == palpite:
        print('Você acertou!')
        break
    elif palpite < numero:
        print('O número palpite foi abaixo do número!')
    elif palpite > numero:
        print('O seu palpite foi acima do númeor!')
