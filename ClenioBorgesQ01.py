# IFPE
# Aluno: Clênio Borges Barboza Filho 
# Matrícula: 20192EWBJ0221
# Introdução a programação 2019.2
# Professor: Francisco
# Prova 01
# Questão 01 - Faça um programa em Python que realiza o cadastro de um professor no IFPE 
# utilizando variáveis na memória e, ao final do cadastro, o programa mostra na tela as 
# informações recebidas (utilizando na impressão a primeira letra de cada palavra como maiúscula). 
# Considere as informações solicitadas pelo programa: Nome, Idade, Salário, Nome da disciplina que o professor ministra 
# (considere que é apenas uma para facilitar a implementação).

print("\n\nCadastro de professor novo, considerando o usuário como o professor!\n\n")
nome=str(input("Informe seu nome completo: "))
idade=int(input("Informe sua idade: "))
salario=float(input("Informe seu salário: "))
disciplina=str(input("Qual a disciplina que você ministra? "))

print(f"\nSeja bem-vindo professor, {nome.title()}, segue abaixo seus dados para conferência!\n")
print(f"Professor {nome.title()}, {idade} anos, recebe R${salario:.2f} e minsitra a disciplina de {disciplina.title()}\n\n")