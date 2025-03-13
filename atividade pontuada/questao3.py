import os 
os.system("clear")

#inserir dados

numero_um = (int(input("digite o primeiro valor: ")))
numero_dois =(int(input("digite o segundo valor: ")))

#exibir dados

if numero_um == numero_dois :
   soma = numero_um + numero_dois
   print(f"valor da soma:(soma)")
else: 
 multiplicacao = numero_um * numero_dois
print(f"valor da multiplicacao: (multiplicacao)")

print(f"valor do numero_um: (numero_um)")
print(f"valor do numero_dois: (numero_dois)")
