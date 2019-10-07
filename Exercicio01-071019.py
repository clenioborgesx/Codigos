lista01=[]

while True:
    palavras=input("Informe uma palavra ou digite ENTER para finalizar: ")
    if palavras == "":
        break
    lista01.append(palavras.lower())
for i in lista01:
    print("Palavra: ",i)