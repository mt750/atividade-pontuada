import os
os.system("clear")

cor = input("digite a cor do cd (verde, azul,amarelo,vermelho): ")

#verificacao do preco com base na cor
if cor == "verde":
    preco = 10.00
elif cor == "azul":
    preco = 20.00
elif cor == "amarelo":
    preco = 30.00
elif cor == "vermelho":
    preco = 40.00
else:
    preco = None

# exibicacao do resultado
if preco is not None:
    print(f"o preco do cd de cor {cor} e R${preco:.2f}")
else:
    print("cor invalida. por favor , insira uma cor valida(verde,azul,amarelo,vermelho).")