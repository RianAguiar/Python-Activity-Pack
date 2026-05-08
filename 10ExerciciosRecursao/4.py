def calcular(base, expoent):
    if expoent == 0:
        return 1
    return base * calcular(base, expoent - 1)

base = int(input("Digite base: "))
expoent = int(input("Digite expoente: "))
print(calcular(base, expoent))