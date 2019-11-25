arquivoIN = open("arq1.txt","r")
produto = 1
for i in arquivoIN.readlines():
    produto *= int(i)
arquivoIN.close()
arquivoOUT = open("arq2.txt",'w')
arquivoOUT.write(str(produto))
arquivoOUT.close()