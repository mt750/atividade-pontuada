import os
os.system("clear")

#inserir dados
numero_um = int(input("digite o numero um: "))
numero_dois = int(input("digite o numero dois: "))
numero_tress = int(input("digite o numero tres: "))
soma =  numero_um + numero_dois 
if soma > numero_dois: 
   
   print("primeiro numero e segundo maior que o terceiro numero")
else:
   print("terceiro numero maior que um e dois")

#exibir dados 
print(f"numero_um escolhido:(numero_um)")
print(f"numero_dois escolhido:(numero_dois)")
print(f"numero_tres escolhido:(numero_tres)")

