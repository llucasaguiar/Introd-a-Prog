# Escreva um algoritmo que permita a leitura dos nomes de
# 5 clubes de futebol e armazene os nomes lidos em um vetor.
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome
# qualquer de clube e depois escrever a mensagem ACHEI,
# se o nome estiver entre os 5 nomes lidos anteriormente
# (guardados no vetor), ou NÃO ACHEI caso contrário.

selecoes = [
    'Malásia',
    'China',
    'Gabão',
    'Malta'
]

selecao = input('Digite a seleção desejada: ')
busca = False

for i in range(len(selecoes)):
    if selecao.upper() == selecoes[i].upper():
        busca = True

if busca:
    print(f'Achei!')
else:
    print(f'Não achei!')