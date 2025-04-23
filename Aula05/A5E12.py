# Determinação do tipo de triângulo.
# Questão: Peça ao usuário para inserir três lados de um triângulo
# e determine se é um triângulo equilátero, isósceles ou escaleno.

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if lado1 == lado2 == lado3:
    print(f'O triângulo é equilátero.')
elif lado1 != lado2 != lado3:
    print(f'O triângulo é escaleno.')
else:
    print(f'O triângulo é isósceles.')