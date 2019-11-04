def mediapopulacao(salario,quantidadefilhos):
    somatorio=0.0
    contador=0
    for i in range(len(salario)):
        somatorio+=salario[i]
        contador+=quantidadefilhos[i]
    mediapopular=somatorio/contador

    return mediapopular
def mediafilhos(quantidadefilhos,i):
    somatorio=0.0
    for j in range (0,len(quantidadefilhos)):
        somatorio+=quantidadefilhos[j]
    if j==0:
        mediafil=somatorio/1
    else:
        mediafil=somatorio/j
    return mediafil

def ordenasalario(salario):
    # cópia do salario
    r = salario
    # laço de ordenação do salario01
    for i in range(1, len(salario)):
        # laço de comparação do salario
        for j in range(i,0,-1):
            # compara se o item é maior que outro
            # Insertion sort?
            if(r[j]<r[j-1]):
                # atribui uma auxiliar para salario
                # Troca de número
                raux = r[j]
                r[j] = r[j-1]
                r[j-1] = raux
            else:
                break
    return r
def verificasalario(salario,quantidadefilhos):
    contador=0
    for i in range(len(salario)):
        if (salario[i]/quantidadefilhos[i])<=380.00:
            contador+=1
    return contador
salarios=0.0
salario=[]
quantidadefilhos=[]
i=0
while True:
    salarios=input("Qual o valor do seu salário? ")
    if salarios =="":
        mediapop=mediapopulacao(salario,quantidadefilhos)
        mediaf=mediafilhos(quantidadefilhos,i)
        ordenas=ordenasalario(salario)
        maior=ordenasalario[i] #CORRIGIR
        menor=ordenasalario[0] #CORRIGIR
        situacao=verificasalario(salario,quantidadefilhos)
        print("A média salarial da população é: ", mediapop)
        print("A quantidade média de filhos da população é: ", mediaf)
        print("O maior salário e o menor salário são : ",ordenas)
        print("A quantidade de familias recebendo até R$380,00 é: ",situacao)
        break
        
    else:
        salario.append(float(salarios))
        quantidadefilhos.append(int(input("Quantas crianças tem na sua casa? ")))
        i+=1