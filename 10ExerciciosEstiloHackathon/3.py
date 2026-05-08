quantidade = int(input("Quantidade de alimentos: "))

for i in range(quantidade):
    nome = input("Nome do alimento: ")
    peso = float(input("Quantidade em kg: "))
    validade = int(input("Validade em dias: "))

    if validade <= 3:
        prioridade = "Prioridade alta"
    elif validade <= 7:
        prioridade = "Prioridade média"
    else:
        prioridade = "Prioridade baixa"

    print(f"{nome} - {prioridade}")