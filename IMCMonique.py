print("Bem vindo,Ao calculador de IMC!")
somapeso=0
somaltura=0
somaimc=0
for item in range(10):
    peso = float (input ("Por favor,Digite seu peso:"))
    altura = float (input ("Por favor,Digite sua altura:"))
    imcDoUsuario = peso/(altura*altura) 

    print("O ImcDoUsuario é: {:.4f}".format(imcDoUsuario))
    if imcDoUsuario < 17:               # Monique, lembra que a indentação importa no python?s
        print("Muito abaixo do peso")   # Eu vou identar algumas e tu continua, vou destacar onde tem erro com (::) okay?
    elif imcDoUsuario < 18.5:
        print("Abaixo do peso")
    elif imcDoUsuario < 25:
        print("Peso normal")    
    elif imcDoUsuario < 30:
        print("Obeso")
    elif imcDoUsuario < 35:
         print("Obesidade I")
    elif imcDoUsuario < 40:
        print("Obesidade II")
    else:
        print("Obesidade III")
    somapeso=somapeso+peso
    somaltura=somaltura+altura
    somaimc=somaimc+imcDoUsuario
mediaDoImcDoUsuario = (somaimc)/10
mediaDoPeso = (somapeso)/10
mediaDaAltura = (somaltura)/10
print("A media do imcDoUsuario é : {:.4f}".format(mediaDoImcDoUsuario))
print("A media do peso é: {:.4f}".format(mediaDoPeso))
print("A media da altura é: {:.4f}".format(mediaDaAltura))