"essa questão foi feito com auxilio de IA pq n sabia a função lambda"

qtd = int(input("Quantidade de chamados: "))

chamados = []

for i in range(qtd):
    espera = float(input(f"Tempo de espera do chamado {i+1}: "))
    impacto = int(input(f"Impacto do chamado {i+1} (1 a 5): "))
    usuarios = int(input(f"Usuários afetados do chamado {i+1}: "))

    prioridade = espera + (impacto * 10) + (usuarios * 2)

    if prioridade <= 30:
        classificacao = "Baixa prioridade"
    elif prioridade <= 60:
        classificacao = "Prioridade média"
    elif prioridade <= 100:
        classificacao = "Alta prioridade"
    else:
        classificacao = "Crítica"

    chamados.append((i + 1, prioridade, classificacao))

chamados.sort(key=lambda x: x[1], reverse=True)

print("\nChamados ordenados:")

for chamado in chamados:
    print(f"Chamado {chamado[0]} - {chamado[1]:.0f} pontos - {chamado[2]}")