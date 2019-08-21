# Programa para calcular o IMC (índice de massa corporal) de um ser humano. O programa recebe a altura e o peso da pessoa
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

altura=float(input("Informe sua altura: "))
peso=float(input("Informe seu peso: "))
imc=float((peso)/(altura**2))
if imc < 17:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta muito abaixo do peso!")
elif imc >= 17 and imc <= 18.49:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta abaixo do peso!")
elif imc >= 18.5 and imc <= 24.99:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta no peso ideal!")
elif imc >= 25 and imc <= 29.99:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta acima do peso!")
elif imc >= 30 and imc <= 34.99:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta com obesidade nivel 1!")
elif imc >= 35 and imc <= 39.99:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta com obesidade nivel 2(Severa) Procure um especialista!")
elif imc >= 40:
    print("Seu IMC eh: ",round(imc,2),"\nVoce esta com obesidade nivel 3(Morbida) Procure um especialista URGENTE!")