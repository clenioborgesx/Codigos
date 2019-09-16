# IFPE
# Aluno: Clênio Borges Barboza Filho 
# Matrícula: 20192EWBJ0221
# Introdução a programação 2019.2
# Professor: Francisco
# Prova 01
# Questão 03 - Faça um programa Python para ler uma sequência de números inteiros. 
# A leitura deve parar quando um número negativo for lido. Ao final, o programa deve 
# imprimir (nesta ordem): a. A quantidade total de números lidos; b. O maior e o menor 
# número lido; c. A média de todos os números lidos; d. A quantidade de números que são 
# múltiplos de 6; e. A média aritmética dos dois últimos números digitados.
# Declaração das variáveis
maior=int(0)
menor=int(99999999999999999999999999999999999999999999999)
contador=int(0)
soma=int(0)
media=float(0.0)
contmulti=int(0)
ultimo=int(0)
penultimo=int(0)
mediaultimos=float(0)
# Iniciando a recepção dos numeros
numero=int(input("Informe o primeiro número: "))

if numero <0:
    print(f"a) Você informou 1 números!")
    print(f"b) O maior número foi 0 e o menor número foi 0")
    print(f"c) A média dos números informados foi: 0")
    print(f"d) Dos números informados, 0 eram multiplos de 6!")
    print(f"e) A média dos dois últimos números informados foi: 0")
else:
    contador+=1
    soma2=soma
    soma+=numero
    ultimo=numero
    penultimo=(soma-soma2)-numero
    if numero%6 == 0:
        contmulti+=1
    if numero > maior:
        maior=numero
    if numero<menor:
        menor=numero
    while numero > 0:
        numero=int(input("Informe o número ou um numero negativo para parar: "))
        if numero>0:
            contador+=1
            soma2=soma-numero
            soma+=numero
            penultimo=ultimo
            ultimo=numero
            if numero%6 == 0:
                contmulti+=1
            if numero > maior:
                maior=numero
            if numero<menor:
                menor=numero
    media=float(soma/contador)
    mediaultimos=float((ultimo+penultimo)/2)
    print(f"a) Você informou {contador} números!")
    print(f"b) O maior número foi {maior} e o menor número foi {menor}")
    print(f"c) A média dos números informados foi: {media:.2f}")
    print(f"d) Dos números informados, {contmulti} eram multiplos de 6!")
    print(f"e) A média dos dois últimos números informados foi: {mediaultimos:.2f}")
