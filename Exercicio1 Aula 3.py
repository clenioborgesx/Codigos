# Clênio Borges
#IFPE-2019.2

print("\n\n\nEsse programa serve para verificar qual o numero maior dos 3 dados pelo user\n\n\n")
num1=int(input("Informe o primeiro numero:"))
num2=int(input("Informe o segundo numero:"))
num3=int(input("Informe o terceiro numero:"))
if num1>num2 and num1>num3:
    print("O maior numero eh: ", num1)
elif num2>num1 and num2>num3:
    print("O maior numero eh: ", num2)
else:
    print("O maior numero eh: ", num3)