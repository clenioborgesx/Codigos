# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

resultado=0
print("\n\n\nO programa vai o valor dos catetos e resolvera sua hipotenusa! (x1² + x2²=hipotenusa²) \n\n\n\n")
valor1=float(input("Informe o primeiro cateto: \n"))
valor2=float(input("Informe o segundo cateto: \n"))
#valor3=float(input("Informe o terceiro valor: \n"))
resultado= round(((valor1**2)+(valor2**2))**(1/2),5)
print("\n\nA hipotenusa eh:",resultado)