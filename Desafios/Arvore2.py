# O programa faz desenhos na tela, nesse caso desenha árvore
#   
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
base=int(input("Por favor informe a base (maior que 0 e menor que 30): "))
print()
if base>29:
    print("Entrada inválida!")
else:
    espacos=base
    intervalo=int(base+(base/2))
    if base%2 == 0:
        i=1
        print(" "*(espacos+1),"#"*i)
        for i in range (2,base+1,2):
            print(" "*espacos,"#"*i)
            espacos-=1
            i+=1
    else:
        for i in range (1,intervalo,2):
            print(" "*espacos,"#"*i)
            espacos-=1
print()