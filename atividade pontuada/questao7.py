import os

os.system("clear")

# solicitando dados

produto = input("digite a descricao do produto: ")
quantidade = int(input("digite a quantidade adquirida: "))
preco_unitario = float(input("digite o preco unitario: "))

# calculando total sem desconto
total = quantidade*preco_unitario

#determinando o percentual com desconto

if quantidade <= 5: desconto = 2

elif quantidade <= 10: desconto = 3 

else:
    desconto = 5

# calculando valor do desconto
desconto = (desconto /100)*total

# calculando o total a pagar
total_a_pagar = desconto - total