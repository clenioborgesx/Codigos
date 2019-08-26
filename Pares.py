# O código mostra os 10 primeiros números pares ao usuário
#
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

print("\nOs 10 primeiros números pares são:\n")
for NumPar in range(2,22,2):
    print(NumPar)

# Segunda forma de fazer

NumPar=2
print("\nOs 10 primeiros números pares são:\n")
for i in range(0,10,1):
    print(NumPar)
    NumPar+=2

# Terceira forma de fazer

print("\nOs 10 primeiros números pares são:\n")
for i in range(0,20,1):
    NumPar = i+2
    if NumPar%2 == 0:
        print(NumPar)