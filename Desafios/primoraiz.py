
num = int(input('Digite um numero: '))
raiz = (num**0.5)
if num==2 or num==3:
      print("Primo")
else:
        for i in range(1,int(raiz),1):
                pMod = num%i
                print(f"{i},{raiz},{num}")
                if pMod == 0:
                        Composto+=1
                else:
                        primo+=1
        if composto>1:
                print('Composto')
        else:
                print("Primo")