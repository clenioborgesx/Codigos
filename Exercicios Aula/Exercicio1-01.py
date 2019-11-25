# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# Lista 01
# 01- Exercico recebe dois valores do user e mostra a diferença entre eles:

maior=0                                                     # Iniciando a variável maior com zero, para que qualquer numero seja maior ou igual caso não seja negativo
menor=10000000000000000000000                               # Iniciando a variável menor com um numero grande para que qualquer numero seja menor que ele
for i in range(0,2,1):                                      # Laço que faz a recepção dos valores informados pelo user e confere
    valor=int(input("Informe o valor {}: " .format(i+1)))   # Aqui os usuários informam os valores que desejarem
    if valor>maior:                                         # Compara o valor informado com a variável maior
        maior=valor                                         # Atribui a variável maior qualquer numero acima de zero
        if valor<=menor:                                    # Confere se o número é menor que a variável menor declarada antes do laço
            menor=valor                                     # Atribui a variável menor o valor que o usuário informou caso seja menor que a variável, para caso os números sejam iguais
    else:                                                   # Caso o número não seja maior que o zero
        menor=valor                                         # Menor assume o valor de valor, casos para 0
valor=maior-menor                                           # Usei a mesma variável para aproveitar, que faz a conta para a diferença entre os números
print("A diferença entre eles é: ",valor)                   # Impressão da diferença
print("O maior é: ",maior)                                  # Impressão do resultado maior
print("O menor é: ",menor)                                  # Impressão do resultado menor