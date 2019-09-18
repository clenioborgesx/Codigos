
# Entrada do usuário um número qualquer
for num in range (1,10000,1):
# Calcula a raíz para otimizar a busca do programa, senão ele faria a verificação até o número e demoraria mais:
# Observe que a raiz é inteira, pois o laço for não trabalha com FLOAT e só nos é útil por enquanto o valor inteiro
    composto=0
    raiz=int(num**0.5)
    for i in range(2,raiz+1,1):
            # Se o número dividido por i tiver resto 0 é porque é divisível por algum número, então ele incrementa ao contador composto
        if num%i == 0:
            composto+=1
        # Se o contador tiver 1 numero é porque foi divisivel então o número é composto
    if composto >= 1:
        print(f"O número {num} é composto!")
        composto=0
    else:
            # Caso contrário ele só pode ser primo:
        print(f"O número {num} é primo!")