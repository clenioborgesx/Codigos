# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

print("\n\n\nEsse programa serve para verificar qual o numero maior dos 3 dados pelo user\n\n\n")
num1=int(input("Informe o primeiro numero:"))
num2=int(input("Informe o segundo numero:"))
num3=int(input("Informe o terceiro numero:"))
maior=0
menor=0
medio=0
cont=0
for cont in range(3):
    if num1>num2:
        if num1>num3:
            maior=num1
            medio=num3
            menor=num2
        else:
            menor=num2
            medio=num1
            maior=num3
    else:
        if num2>num3:
            if num1>num3:
                maior=num2
                medio=num1
                menor=num3
        else:
            maior=num2
            medio=num3
            menor=num1
if num1>num2 and num1>num3:
    print("O maior numero eh: ", num1)
elif num2>num1 and num2>num3:
    print("O maior numero eh: ", num2)
else:
    print("O maior numero eh: ", num3)
print("\n\n Do maior para o menor: \n\n",maior,medio,menor)