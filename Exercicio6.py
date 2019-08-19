resultado=0
print("\n\n\nO programa vai pedir o valor do salário e acrescentara 4% de bonus! (x1+(x1*0.04)=salario novo) \n\n\n\n")
valor1=float(input("Informe o salario: \n"))
valor2=float(input("Informe o total de vendas: \n"))
#valor3=float(input("Informe o terceiro valor: \n"))
resultado= round(valor1+(valor2*0.04),2)
print("\n\nO salario sera:",resultado)