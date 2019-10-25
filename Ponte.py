# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# editado: Matheus Patriota

# Welcome
print("\n\nO programa serve para dizer quantos metros de cabo de aço será utilizado na ponte:\n\n")

# variables and inputs
c1=int(input("Qual o comprimento da ponte em KM? :\n")) #Linha recebe o comprimento da ponte dada pelo usuário em KM
c2=float((c1/2)*1000)                                   #Linha converte o comprimento informado pelo usuário em metro
c3=int(c2)                                              #
h1=float(c2/20)                                         #Medida da haste
h2=int(h1)                                              #
i=0                                                     #Linha atribui 5 para a variavel i que será usada como contador
soma=0                                                  #Linha que inicia a var soma
vet=[i]                                                   #

# logic
for i in range(5):                                      #Nó que dá as medidas dos cabos
    vet.append(i+1)                                     #
    vet[i]=float(((c2**2)+(h1**2))**0.5)                # Atrbui ao vetor o comprimento do cabo em cada extensão
    c2=float(c2-(c3*0.2))                               #
    h1=float(h1-(h2*0.2))                               #
    soma=float(soma+vet[i])                             #
    print('O cabo',i+1, 'mede:',vet[i])                 
    
else:                                                   #
    soma=int(4*soma)                                    #
    print('Você precisará de',soma,'m de cabo')         #