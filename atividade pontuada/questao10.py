import os

os.system("clear")

import os

os.system("clear")

preco_gasolina = 6.59
preco_alcool = 3.79

# Leitura dos dados
litros = float(input("Digite o número de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ")

# Verificando o tipo de combustível e calculando o valor a ser pago
if combustivel == 'A':  # Álcool
    valor_total = litros * preco_alcool
elif combustivel == 'G':  # Gasolina
    valor_total = litros * preco_gasolina
else:
    print("Tipo de combustível inválido!")
    exit()

# Exibindo o valor a ser pago
print(f"O valor a ser pago é R$ {valor_total:.2f}")
