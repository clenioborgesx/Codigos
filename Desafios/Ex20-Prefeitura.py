def mediapopulacao(media,quantidadefilhos,i):
    somatoriomedia=0.0
    somatoriofilhos=0
    contador=i
    for j in range(len(quantidadefilhos)):
        somatoriomedia+=media[j]
        somatoriofilhos+=quantidadefilhos[j]
    mediapopular=somatoriomedia/contador
    mediafil=somatoriofilhos/contador

    return (mediapopular,mediafil)

salarios=0.0
salario=[]
quantidadefilhos=[]
media=[]
situacao=0
menor=0
maior=0
i=0

while True:
    salarios=input("Qual o valor do seu salário? ")
    if salarios =="":
        mediapop=mediapopulacao(media,quantidadefilhos,i)
        print(f"A média salarial da população é: {mediapop[0]:.2f}")
        print(f"A quantidade média de filhos da população é {mediapop[1]:.2f}")
        print(f"O maior salário é {maior} o menor salário é {menor} ")
        print(f"{(float(situacao/i)*100)}% familia(as) está(ão) recebendo até R$380,00")
        break
        
    else:
        salario.append(float(salarios))
        quantidadefilhos.append(int(input("Quantas crianças tem na sua casa? ")))
        media.append(float(salario[i]/quantidadefilhos[i]))

        if salario[i]<380.0:
            situacao+=1

        if salario[i]>=salario[i-1]:
            maior=salario[i]
            
        else:
            menor=salario[i]
        i+=1