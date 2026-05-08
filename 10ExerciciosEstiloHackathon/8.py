qtd = int(input("Quantidade de salas: "))

for i in range(qtd):
    nome = input("Nome da sala: ")
    capacidade = int(input("Capacidade máxima: "))
    atual = int(input("Quantidade atual de pessoas: "))

    porcentagem = (atual / capacidade) * 100

    if porcentagem <= 50:
        classificacao = "Baixa ocupação"
    elif porcentagem <= 80:
        classificacao = "Ocupação moderada"
    elif porcentagem <= 100:
        classificacao = "Sala quase cheia"
    else:
        classificacao = "Superlotada"

    print(f"{nome} - {porcentagem:.2f}% - {classificacao}")