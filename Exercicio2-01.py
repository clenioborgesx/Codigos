# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# Lista 01
# 02 - Exercico recebe duas notas e mostra a média ponderada com pesos diferentes:

nota1=float(input("Informe a nota 01: "))                     # Aqui o usuário informa a primeira nota
nota2=float(input("Informe a nota 02: "))                     # Aqui o usuário informa a segunda nota
# Nota1 tem peso 3 e nota2 tem peso 1 e a soma dos pesos é 4
notafinal=float(((nota1*3)+(nota2*1))/4)                      # A média é somatório=nota*peso dividido pelo somatório=pesos
print("A média do aluno é: {:.2f} ".format(notafinal))                       # Impressão da média