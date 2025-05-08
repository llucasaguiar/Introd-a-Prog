# Crie um programa para cadastrar filmes utilizando
# o conceito de vetores, matrizes e funções.

#Introdução de mais um item no menu e do try-except-exception
# Instalação do Loguru e aplicação do logger
# Logger serve para registrar e arquivar informações, ex.: comportamento da minha aplicação.

import time
from loguru import logger

bd_filmes = []

def cadastrar_filmes(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

def lista_filmes(bd):
    logger.info('Listagem de filmes.')
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filme(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd

def salvar_filmes(bd):
    with open('bd_filmes.txt', 'w', encoding='utf-8') as arquivo:
        for i in range(len(bd)):
            logger.info(f'Salvando os filmes {bd[i][0]}')
            arquivo.write(f'{bd[i][1]}, {bd[i][0]}\n')

while True:
    print('1 - Cadastrar Filme')
    print('2 - Listar Filmes')
    print('3 - Alterar Filme')
    print('4 - Salvar Filmes')

    try:
        op = int(input('Digite sua opção: '))
    except Exception as e:
        logger.error(f'Erro: {e}')
        logger.info('Digite um valor numérico.')
        op = -1

    if op == 1:
        logger.info('Iniciando o cadastro de filme.')
        titulo = input('Digite o titulo do filme: ')
        ano = int(input('Digite o ano do filme: '))
        bd_filmes = cadastrar_filmes(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano
        )
        print('Filme cadastrado!')

    elif op == 2:
        logger.info('Iniciando de listagem de filmes.')
        lista_filmes(bd_filmes)
        logger.info('Filmes listados com sucesso!')

    elif op == 3:
        logger.info('Iniciando alteração do filme.')
        lista_filmes(bd_filmes)
        i = int(input('Qual filme deseja alterar? '))
        titulo = input('Digite o novo título: ')
        ano = int(input('Digite o novo ano: '))
        bd_filmes = altera_filme(
            bd=bd_filmes,
            indice=(i-1),
            titulo=titulo,
            ano=ano
        )
        logger.info('Filme alterado com sucesso!')

        logger.info('Filme cadastrado com sucesso.')

    elif op == 4:
        logger.info('Iniciando persistência dos filmes.')
        salvar_filmes(bd_filmes)
        logger.info('Filmes salvos com sucesso!')
    else:
        print(f'Opção {op} inválida!')

    time.sleep(2)