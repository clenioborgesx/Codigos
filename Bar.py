# Buteco
# O programa serve para calcular uma conta de bar, o garçon informa o valor e a quantidade de produtos consumidos
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

print("\nButeco da Rafa, você entra bom e sai RUIM!\n")
valor =float(input("Informe o valor do produto: "))
contador = 0
while(valor>=0):
    contador+=valor
    print("A conta está em:", contador)
    valor = float(input("Informe o valor do outro produto: (Digite -1 para sair) "))
else:
    print("A conta deu: {:.2f} ".format(contador))