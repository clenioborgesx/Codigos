# Aluno: Clênio Borges Barboza Filho
# Introdução a programação 2019.2
# Professor: Francisco
# Lista 01
# 04 - Calculo de raio, perímetro e área de uma circunferência, depois do user informar o diâmetro.
pi=float(3.14)
diametro=float(input("Informe o diâmetro que deseja em cm: "))
raio=diametro/2
peri=2*pi*raio
area=pi*(raio**2)
print(f"O raio é {raio:.2f}cm, o perímetro é {peri:.2f}cm e a área é {area:.2f}cm")