resultado=0
print("\n\n\nO programa vai pedir o valor do produto e dara desconto de 10%! (x1-(x1*0.1)=preço novo) \n\n\n\n")
valor1=float(input("Informe o preco do produto: \n"))
#valor2=float(input("Informe o segunda nota: \n"))
#valor3=float(input("Informe o terceiro valor: \n"))
resultado= round(valor1-(valor1*0.1),2)
print("\n\nA preco com desconto eh:",resultado)