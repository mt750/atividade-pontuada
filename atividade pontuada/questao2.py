import os
os.system("clear")

#inserir dados

estado_civil = (str(input("digite seu estado civil: ")))
sexo = (str(input("digite seu sexo:  ")))
if estado_civil == "casada":
 dados = (str(input("digite quanto tempo de casada possui: ")))

else:
 print("obrigado pelas informacoes")

 #exibindo dados
 print(f"estado_civil:(estado_civil): ")
 print(f"sexo:(sexo): ")
 print(f"dados:(dados)")
