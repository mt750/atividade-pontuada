import os

os.system("clear")

primeira_nota = float(input("digite sua primeira nota: "))
segunda_nota = float(input("digite sua  segunda nota: "))


media = (primeira_nota + segunda_nota)  /2

print()
print("sua media e: ", media)

if media >=6:
    print("aprovado")
elif media == 4 or 5:
    print("recuperacao")
else:
    print("reprovado")