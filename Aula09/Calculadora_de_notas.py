# Crie um programa que peça ao usuário para
# inserir várias notas de um aluno e calcule a média.
# Utilize um loop para continuar pedindo notas até que
# o usuário digite um valor específico para encerrar
# a entrada (por exemplo, -1).

notas = []

while True:
    print('Adicione a nota ou digite -1 para sair.')

    valor = int(input('Digite a nota ou -1: '))

    if valor == -1:
        break
    elif 0 <= valor <= 10:
        notas.append(valor)
    else:
        print(f'O valor {valor} é inválido!')

somatorio = 0

for i in range(len(notas)):
    somatorio = somatorio + notas[i]

media = somatorio / len(notas)

print(f'A média final é: {media}')
print(f'As notas são: {notas}')