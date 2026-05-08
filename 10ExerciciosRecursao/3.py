n = int(input("digite o numero: "))
def sub(n):
    print(n)
    if n == 0:
        return 1
    return sub(n - 1)
sub(n)
