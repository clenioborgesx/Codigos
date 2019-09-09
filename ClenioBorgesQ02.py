# IFPE
# Aluno: Clênio Borges Barboza Filho 
# Matrícula: 20192EWBJ0221
# Introdução a programação 2019.2
# Professor: Francisco
# Prova 01
# Questão 02 - Sabe-se que o valor de um quilowatt-hora (kWh) de energia possui valor 
# base de R$ 0,04 e o valor da conta varia de acordo com o custo de geração a cada mês 
# de acordo com a tabela em anexo. Sabe-se também que o cliente recebe um desconto de 
# acordo com o dia em que realiza o pagamento: 8% caso pague a conta antes do dia 10 do mês, 
# 5% caso pague até o dia 15 e sem desconto caso pague após o dia 15. 
# Faça um programa em Python que recebe a bandeira tarifária do mês e a quantidade de quilowatts-hora 
# consumidos por uma residência no mês. Com base nas informações recebidas calcule e mostre na tela qual
# o valor a ser pago pelo cliente de acordo com a data do pagamento.
print("Bandeiras: \n\n 1- Verde \n 2- Amarela \n 3- Vermelha Patamar 1 \n 4- Vermelha Patamar 2 \n")
bandeira=int(input("Informe a bandeira desse mês(seguindo a tabela acima): "))
while bandeira <1 or bandeira >4:
    print("\n\nO valor informado não confere, tente novamente! (Siga a tabela abaixo)")
    print("\nBandeiras: \n 1- Verde \n 2- Amarela \n 3- Vermelha Patamar 1 \n 4- Vermelha Patamar 2 \n")
    bandeira=int(input("Informe a bandeira desse mês: "))
kwh=int(input("Informe o consumo em KWh: "))
while kwh < 1:
    print("\n\nO valor informado não confere, tente novamente!")
    kwh=int(input("Informe o consumo em KWh: "))
base=float(0.04)
conta=float(0.0)
tarifa=float(0.0)
if bandeira == 1:
    conta=kwh*base
elif bandeira == 2:
    amarela=1.50
    while kwh >100:
        tarifa=(100*base)+amarela
        conta+=tarifa
        kwh-=100
    conta+=(kwh*base)
elif bandeira == 3:
    verm1=4.00
    while kwh >100:
        tarifa=(100*base)+verm1
        conta+=tarifa
        kwh-=100
    conta+=(kwh*base)
elif bandeira == 4:
    verm2=6.00
    while kwh >100:
        tarifa=(100*base)+verm2
        conta+=tarifa
        kwh-=100
    conta+=(kwh*base)

print(f"Sua conta deu: R${conta:.2f}\n")
print(f"Se você pagar antes do dia 10 pagará somente: R${(conta-(0.08*conta)):.2f}")
print(f"Se você pagar depois do dia 10 e antes do dia 15 pagará somente: R${(conta-(0.05*conta)):.2f}")
print(f"Se você pagar depois do dia 15 pagará: R${conta:.2f}\n")