# Programa para verificar se o número é primo utilizando como verificador otimizado sua raiz
# Alunos: Clênio Borges
# Professora: Priscila Souza
# Declaração do contador para o composto
composto = 0
# Entrada do usuário um número qualquer
num = int(input("Informe o número: "))
# Calcula a raíz para otimizar a busca do programa, senão ele faria a verificação até o número e demoraria mais:
# Observe que a raiz é inteira, pois o laço for não trabalha com FLOAT e só nos é útil por enquanto o valor inteiro
raiz = int( num**0.5 )
# Esse laço verifica se o número é par e é diferente de 2, pois se for não tem como ser primo, já se ganha muito tempo assim:
if num%2 == 0 and num != 2:
    print(f"O número {num} é composto!")
# Essa condição é só pra garantir que quando for 1 ou 2 o numero é primo:
elif num == 1 or num == 2 :
    print(f"O número {num} é primo!")
# Caso as outras condições não sejam atendidas, o programa entra nesse laço que fará a verificação dos número 1 por 1 até o valor inteiro da raiz
else:
    # O programa varre de 2 até a raiz do numero informado, 1 a 1:
    for i in range(2,raiz+1,1):
        # Se o número dividido por i tiver resto 0 é porque é divisível por algum número, então ele incrementa ao contador composto
        if num%i == 0:
            composto+=1
    # Se o contador tiver 1 numero é porque foi divisivel então o número é composto
    if composto >= 1:
        print(f"O número {num} é composto!")
    else:
        # Caso contrário ele só pode ser primo:
        print(f"O número {num} é primo!")
    