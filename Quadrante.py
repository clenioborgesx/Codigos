# Esse programa serve para o usuário saber onde se encontra o ponto (x,y) no plano cartesiano
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco

x=int(input("Informe X: "))                                             # O usuário informa o valor de X
y=int(input("Informe Y: "))                                             # O usuário informa o valor de Y
if x == 0 and y == 0 :                                                  # Essa condição testa se o ponto se encontra na origem para evitar os passos seguintes
    print("O ponto esta na origem!")
elif x==0:                                                              # Se o ponto for x=0 estará em cima do eixo das abicissas
    print("O ponto (",x,",",y,") esta no eixo das abcissas!")
elif y==0:                                                              # Se o ponto for y=0 estará em cima do eixo das ordenadas
    print("O ponto (",x,",",y,") esta no eixo das ordenadas!")
else:                                                                   # Caso o ponto não esteja na origem os passos seguintes são executados
    if x>0 and y>=0:                                                    # X positivo e Y positivo ou igual a ZERO = 1º Quadrante
        print("O ponto: (",x,",",y,") esta no primeiro quadrante!")     
    elif y>0 and x<=0:                                                  # X Negativo ou igual a ZERO e Y Positivo = 2º Quadrante
        print("O ponto: (",x,",",y,") esta no segundo quadrante!")
    elif x<0 and y<=0:                                                  # X Negativo e Y Negativo ou igual a ZERO = 1º Quadrante
        print("O ponto: (",x,",",y,") esta no terceiro quadrante!")
    elif y<0 and x>=0:                                                  # X positivo ou igual a ZERO e Y negativo = 1º Quadrante
        print("O ponto: (",x,",",y,") esta no quarto quadrante!")
