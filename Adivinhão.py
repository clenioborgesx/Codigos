# O programa tem que descobrir o número que o usuário pensou fazendo perguntas!
#   
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# editado: Matheus Patriota

comecoUser = 0
fimUser = 100

lista = list(range(fimUser+1))
numero = int(fimUser/2)
comeco = comecoUser
fim = len(lista)-1

print("Pense em um numero entre {:} a {:} ".format(comeco,fim-1))
while True:

  entrada = input("Seu numero é maior, menor ou igual a {:} : ".format(numero))
  # se o numero apresentando for igual o programa deve parar
  if entrada == "igual":
    print("Acertei xD")
    break
  # se o numero apresentado for menor do que o apresentado
  elif entrada == "menor":
    lista = list(range(comeco,numero))
    fim = numero
    if len(lista) <=1:
      numero = lista[0]
    else:
      numero = lista[int(len(lista)/2)]
      fim = lista[len(lista)-1]
  elif entrada == "maior" and numero == fimUser:
    print("numero nao pode ser maior que {:}}".format(fimUser))
  elif  entrada == "maior":
    lista = list(range(numero+1,fim))
    if len(lista) <= 1:
      numero = lista[0]
    else:
      numero = lista[int(len(lista)/2)]
      comeco = lista[0]


    
