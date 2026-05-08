
n = int(input("digite o numero: "))
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)  
print(fatorial(n))