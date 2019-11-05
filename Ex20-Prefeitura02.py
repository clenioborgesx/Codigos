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
    else:
        mediafil=somatorio/(j+1)
    return mediafil

def ordenasalario(salario):
    # cópia do salario
    r = salario
    maior=r[0]
    menor=r[0]
    for i in range(1, len(salario)):
        for j in range(i,0,-1):
            if(r[j]<r[j-1]):
                raux = r[j]
                r[j] = r[j-1]
                r[j-1] = raux
                maior=r[j]
                menor=r[0]
            else:
                break
    return (maior,menor)
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
        situacao=verificasalario(salario,quantidadefilhos)
        print(f"A média salarial da população é: {mediapop:.2f}")
        print(f"A quantidade média de filhos da população é {mediaf:.2f}")
        print(f"O maior salário é {ordenas[0]} o menor salário é {ordenas[1]} ")
        print(f"{(float(situacao/i)*100)}%  das familia(as) está(ão) recebendo até R$380,00")
        break
        
    else:
        salario.append(float(salarios))
        quantidadefilhos.append(int(input("Quantas crianças tem na sua casa? ")))
        i+=1