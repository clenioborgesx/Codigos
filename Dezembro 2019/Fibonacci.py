def fib(num):
    if num==0:
        return (0)
    elif num==1:
        return(1)
    return(fib(num-1)+fib(num-2))


num=int(input("Informe o número para a sequência de Fibonacci: "))
print(fib(num))