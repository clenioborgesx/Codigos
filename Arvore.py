# O programa faz desenhos na tela, nesse caso desenha árvore
#   
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
base=int(input("Por favor informe a base: "))
i=1
j=1
for i in range (base):
    while i<=base:
        print(" ", end="")
        i+=1
    else:
        print("#"*j)
        j+=2
print("\n")