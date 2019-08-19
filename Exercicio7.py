peso1=0
peso2=0
print("\n\n\nO programa vai pedir o peso atual e calculará perca de 15% e acrescimo de 20%!\n\n\n\n")
valor1=float(input("Informe o peso: \n"))
#valor2=float(input("Informe o total de vendas: \n"))
#valor3=float(input("Informe o terceiro valor: \n"))
peso1= round(valor1-(valor1*0.15),2)
peso2= round(valor1+(valor1*0.2),2)
print("\n\nSe emagrecer 15%:",peso1)
print("Se engordar  20%:",peso2)