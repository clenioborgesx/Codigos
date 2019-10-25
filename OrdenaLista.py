# O código ordena uma lista de números de qualquer tipo, nesse caso float
#
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# Criação da função ordena
def ordenalista(lista):
    # cópia da lista
    r = lista
    # laço de ordenação da lista01
    for i in range(1, len(lista)):
        # laço de comparação da lista
        for j in range(i,0,-1):
            # compara se o item é maior que outro
            # Insertion sort
            if(r[j]<r[j-1]):
                # atribui uma auxiliar para lista
                # Troca de número
                raux = r[j]
                r[j] = r[j-1]
                r[j-1] = raux
            else:
                break
    return r
# Lista aleátória para teste - Random List for teste
Lista01 = [15,7,4,-1,0]

ListaOrd = ordenalista(Lista01)

print("Lista Ordenada = ", *ListaOrd)
print("Lista Ordenada = ", ListaOrd)

for i in range(0,len(ListaOrd)):

    print(f"Lista Ordenada[{i}] = {ListaOrd[i]}")