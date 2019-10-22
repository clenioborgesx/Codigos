# Programa para calcular as médias do IMC,  (índice de massa corporal) de um ser humano. 
# O programa recebe a altura e o peso da pessoa
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# editado: Matheus Patriota

# variables
contPeso=0                                                                                                 # Declaração dos Acumuladores: para o peso 
contImc=0                                                                                                  # para o IMC
contAltura=0         
                                                                                      # para a altura
for i in range(10):                                                                                         # Laço de repetição e contagem i é o contador, i começa em 0 e vai até 09
    altura=float(input("Informe a altura do usuário {}: ".format(i+1)))                                    # Recebe a altura informado pelo user
    peso=float(input("Informe o peso do usuário {}: ".format(i+1)))                                        # Recebe o peso informado pelo user
    imc=float((peso)/(altura**2))                                                                          # Calcula o IMC
    contPeso+=peso                                                                                         # Incremento para o acumulador do peso
    contImc+=imc                                                                                           # Incremento para o acumulador do IMC
    contAltura+=altura    
                                                                                     # Incremento para o acumulador da Altura
    if imc < 17:                                                                                           # Linhas abaixo dessa, mostra o IMC ao usuário e informa a situação
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta muito abaixo do peso!\n\n")
    elif imc <= 18.49:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta abaixo do peso!\n\n")
    elif imc <= 24.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta no peso ideal!\n\n")
    elif imc <= 29.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta acima do peso!\n\n")
    elif imc <= 34.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta com obesidade nivel 1!\n\n")
    elif imc <= 39.99:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta com obesidade nivel 2(Severa)\nDeve Procurar um especialista!\n\n")
    else:
        print("O IMC do Usuário {} é: ".format(i+1),round(imc,2),"\nEle esta com obesidade nivel 3(Morbida)\nDeve procurar um especialista URGENTE!\n\n")
                                                                                                            # Fim da impressão do IMC e situação 
    i+=1      
                                                                                                  # Incremento do contador que mantem o laço
# variables
medPeso= float(contPeso/i)                                                                                  # Calculo da media do peso
medAltura=float(contAltura/i)                                                                               # Calculo da media da altura
medImc=float(contImc/i)  
                                                                                   # Calculo da media do IMC
# output
print("A média do Peso é: {:.2f}".format(medPeso))                                                          # Impressão dos resultados
print("A média de Altura é: {:.2f}".format(medAltura))                                                      # Impressão dos resultados
print("A média do IMC é: {:.2f}".format(medImc))                                                            # Impressão dos resultados
print("\n\n")                                                                                               # Pula linhas por organização
        