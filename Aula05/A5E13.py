# Cálculo de imposto.
# Questão: Peça ao usuário para inserir seu salário mensal.
# Calcule o imposto de renda com base no seguinte: até R$2000, isento;
# de R$2000,01 até R$3500, 10%; acima de R$3500, 15%.

salario = float(input('Insira o valor do seu salário mensal: '))

if salario <= 2000:
    print(f'Você é isento do imposto de renda.')
elif 2000 < salario <= 3500:
    imposto = salario * 0.1
    print(f'Você pagará R$ {imposto} de imposto de renda.')
elif salario > 3500:
    imposto = salario * 0.15
    print(f'Você pagará R$ {imposto} de imposto de renda.')
else:
    print(f'Valor inválido!')