# Esse programa serve para o usuário saber onde se encontra o ponto (x,y) no plano cartesiano
# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# editado: Matheus Patriota

#variables 
x=int(input("Informe X: "))   
y=int(input("Informe Y: "))

# logic
if x == 0 and y == 0 :                                                
    print("O ponto esta na origem!")
elif x==0:                                                            
    print("O ponto (",x,",",y,") esta no eixo das abcissas!")
    print("O ponto (",x,",",y,") esta no eixo das ordenadas!")
else:                                                                   
    if x>0 and y>=0:                                                    
        print("O ponto: (",x,",",y,") esta no primeiro quadrante!")     
    elif y>0 and x<=0:                                                  
        print("O ponto: (",x,",",y,") esta no segundo quadrante!")
    elif x<0 and y<=0:                                                 
        print("O ponto: (",x,",",y,") esta no terceiro quadrante!")
    elif y<0 and x>=0:                                                  
        print("O ponto: (",x,",",y,") esta no quarto quadrante!")
