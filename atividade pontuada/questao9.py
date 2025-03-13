import os

os.system("clear")

# Entrada de dados
renda_mensal = float(input("Informe a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Informe o valor total do empréstimo solicitado: R$ "))
numero_prestacoes = int(input("Informe o número de prestações desejado: "))

    # Calculando o valor da prestação
valor_prestacao = valor_emprestimo / numero_prestacoes

    # Verificando se o empréstimo pode ser concedido
if valor_emprestimo <= 10 * renda_mensal and valor_prestacao <= 0.30 * renda_mensal:
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo não pode ser concedido!")

