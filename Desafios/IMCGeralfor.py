# Programa para calcular as médias do IMC,  (índice de massa corporal) de um ser humano. 
# O programa recebe a altura e o peso da pessoa
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

contPeso=0
contImc=0
conAltura=0
vet=[]
contador=0
for i in range(10):
    vet.append(i+1)
    altura=float(input("Informe a altura do usuário {:0}: ".format(i+1)))
    peso=float(input("Informe o peso do usuário {:0}: ".format(i+1)))
    imc=float((peso)/(altura**2))
    vet[i]=imc
    contPeso+=peso
    contImc+=imc
    conAltura+=altura
    contador+=1
for i in range(10):
    vet.append(i+1)
    if vet[i] < 17:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta muito abaixo do peso!\n\n")
    elif vet[i] >= 17 and vet[i] <= 18.49:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta abaixo do peso!\n\n")
    elif vet[i] >= 18.5 and vet[i] <= 24.99:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta no peso ideal!\n\n")
    elif vet[i] >= 25 and vet[i] <= 29.99:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta acima do peso!\n\n")
    elif vet[i] >= 30 and vet[i] <= 34.99:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta com obesidade nivel 1!\n\n")
    elif vet[i] >= 35 and vet[i] <= 39.99:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta com obesidade nivel 2(Severa) Deve Procurar um especialista!\n\n")
    elif vet[i] >= 40:
        print("O IMC do Usuário {:0} é: ".format(i+1),round(vet[i],2),"\nEle esta com obesidade nivel 3(Morbida) Deve procurar um especialista URGENTE!\n\n")
medPeso= float(contPeso/contador)
medAltura=float(conAltura/contador)
medImc=float(contImc/contador)
print("A média de Peso dos user é: {:.2f}".format(medPeso))
print("A média de Altura dos user é: {:.2f}".format(medAltura))
print("A média de IMC dos user é: {:.2f}".format(medImc))
        