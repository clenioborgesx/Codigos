# O programa recebe as notas dos alunos e informa quantos aprovaram, reprovaram e foram pra final
#  
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
aprovado=0                                                                                     # Variável contadora de aprovados
final=0                                                                                        # Variável contadora de alunos na final
reprovado=0                                                                                    # Variável contadora de reprovados
soma=0                                                                                         # Variável que receberá a soma das notas
nota=0                                                                                         # Variável que recebe as notas para o laço
i=0                                                                                            # Contador para a média dos alunos
while nota >=0:                                                                                # Laço de repetição até que nota seja negativa
    nota=float(input("\nInforme a nota do aluno {} (ou -1 para finalizar): ".format(i+1)))     # Usuário informa a nota do aluno 0 a 10
                                                                                               # i começa em 0 e vai até onde o user informar
    if nota >= 8.5:                                                                            # Inicio do teste para aprovado ou não e imprime o conceito do aluno e a nota
        print("O aluno {} está no conceito A, sua nota é: ".format(i+1),round(nota,2))
        aprovado+=1
    elif nota >= 7.0:
        print("O aluno {} está no conceito B e sua nota é: ".format(i+1),round(nota,2))
        aprovado+=1
    elif nota >= 5.0:
        print("O aluno {} está no conceito C e sua nota é: ".format(i+1),round(nota,2))
        final+=1
    elif nota >= 3.0:
        print("O aluno {} está no conceito D e sua nota é: ".format(i+1),round(nota,2))
        final+=1
    elif nota>=0:
        print("O aluno {} está no conceito E e sua nota é: ".format(i+1),round(nota,2))
        reprovado+=1
    else:                                                                                      # Laço que muda para -1 o valor da nota caso o user digite um numero menor qu -1
        nota=(-1)
    soma += nota                                                                               # Somatório das notas
    i+=1                                                                                       # Incremento do contador i que diz o numero do aluno e serve para calcular a média
else:
    soma+=1                                                                                    # Quando o usuário digitar -1 na soma é acrescentado 1 para não dar erro na média
    i-=1                                                                                       # Subtrai-se 1 para o contador não reconhecer a nota negativa como um aluno
    mediaturma= float(soma/i)                                                                  # Laço calcula a média da turma
    print("\n{} alunos tiveram a nota lançada!".format(i))                                     # A partir daqui as médias são impressas
    print("\nA média da turma é: {:.2f}".format(mediaturma))
    print("O total de alunos aprovados é: {}".format(aprovado))
    print("O total de alunos na final é: {}".format(final))
    print("O total de alunos reprovados é: {}".format(reprovado))
    print("\n\n")