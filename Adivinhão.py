respota = input("o número que você pensou é menor que 101?")
numero = 100

contador = 0
contadorMenor = 0
respostaMenor = 0
while respota == "sim":
    valor = 100
    contador += 10
    numero = valor - contador 
    print("O número que você pensou é menor que ", str(valor - contador)) 
    respota = input()
while respota == "nao":
    print("O número que você pensou é maior que ", str(numero))
    respostaMenor = input()
    while respostaMenor == "sim":
        contadorMenor += 1
        print("O número que você pensou é maior que ", str(numero + contadorMenor))
        respostaMenor = input()
    while respostaMenor == "nao":
        print("O número que você pensou é", numero + contadorMenor)
        break
    break
