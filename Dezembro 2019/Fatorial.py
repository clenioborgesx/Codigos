# Função recursiva do fatorial
def fatorial (num):
    # Condição de quando fatorial(0)=1
    if num == 0:
        return (1)
    # Chamando a função fatorial e multiplicando pelo Numero do user
    # e decrementando até o numero ser zero e atender a condição anterior
    return( num * fatorial (num-1))

num=int(input("Informe o número que deseja encontrar o Fatorial: "))
fat=1
# Fatorial sendo feito pelo laço for para demonstração
for i in range(num,-1,-1):
    # Condição de quando fatorial(0)=1
    if i==0:
        fat*=1
        break
    # Condição para o fatorial o i é decrementado no lugar do número
    fat=fat*i
print(fat)
print(fatorial(num))