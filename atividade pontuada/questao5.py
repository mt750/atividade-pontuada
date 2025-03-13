import os

os.system("clear")

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))
operacao = int(input("qual e o tipo da operacao: "))
resultado = int(input("digite o resultado: "))

match operacao:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"+":
        resultado = primeiro_numero / segundo_numero
    case"+":
        resultado = primeiro_numero - segundo_numero
    case"+":
        resultado = primeiro_numero * segundo_numero

print()
print(f"primeiro numero: {primeiro_numero}")
print(f"operacao: {operacao}")
print(f"segundo numero: {segundo_numero}")
print(f"resultado: {resultado}")