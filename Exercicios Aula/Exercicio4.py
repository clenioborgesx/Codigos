# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

resultado=0
print("\n\n\nO programa vai o valor duas notas e restornara sua media! (x1*0.2 + x2*0.3=media ponderada) \n\n\n\n")
valor1=float(input("Informe o primeira nota: \n"))
valor2=float(input("Informe o segunda nota: \n"))
#valor3=float(input("Informe o terceiro valor: \n"))
resultado= round(((valor1*2)+(valor2*3))/5,2)
print("\n\nA media ponderada eh:",resultado)