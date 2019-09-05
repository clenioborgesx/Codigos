# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# Lista 01
# 05 - Converte segundoa em HH:MM:SS, o user informa uma quantidade de segundos e o programa converte
minu=0
hora=0
sec=0
seg=int(input("Informe a quantidade de segundos que deseja converter: "))
sec=int(seg%60)
minu2=int(seg/60)
minu=int(minu2%60)
hora=int(minu2/60)
print(f"{hora:0>2}:{minu:0>2}:{sec:0>2}")
