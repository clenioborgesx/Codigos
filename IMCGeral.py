# Programa para calcular as médias do IMC,  (índice de massa corporal) de um ser humano. 
# O programa recebe a altura e o peso da pessoa
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

contPeso=0
contImc=0
contAltura=0
contador=0
for i in range(10):
    altura=float(input("Informe a altura do usuário {}: ".format(i+1)))
    peso=float(input("Informe o peso do usuário {}: ".format(i+1)))
    imc=float((peso)/(altura**2))
    contPeso+=peso
    contImc+=imc
    contAltura+=altura
    if imc < 17:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta muito abaixo do peso!\n\n")
    elif imc >= 17 and imc <= 18.49:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta abaixo do peso!\n\n")
    elif imc >= 18.5 and imc <= 24.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta no peso ideal!\n\n")
    elif imc >= 25 and imc <= 29.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta acima do peso!\n\n")
    elif imc >= 30 and imc <= 34.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta com obesidade nivel 1!\n\n")
    elif imc >= 35 and imc <= 39.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta com obesidade nivel 2(Severa)\nDeve Procurar um especialista!\n\n")
    elif imc >= 40:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta com obesidade nivel 3(Morbida)\nDeve procurar um especialista URGENTE!\n\n")
    i+=1
medPeso= float(contPeso/i)
medAltura=float(contAltura/i)
medImc=float(contImc/i)
print("A média do Peso é: {:.2f}".format(medPeso))
print("A média de Altura é: {:.2f}".format(medAltura))
print("A média do IMC é: {:.2f}".format(medImc))
print("\n\n")
        