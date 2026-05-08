qtd = int(input("Quantidade de testes: "))

melhor_pontuacao = -999999
melhor_teste = 0

for i in range(qtd):
    tempo = float(input(f"Tempo do teste {i+1}: "))
    erros = int(input(f"Quantidade de erros do teste {i+1}: "))

    pontuacao = 1000 - tempo - (erros * 50)

    print(f"Teste {i+1}: {pontuacao:.0f} pontos")

    if pontuacao > melhor_pontuacao:
        melhor_pontuacao = pontuacao
        melhor_teste = i + 1

print(f"Melhor teste: Teste {melhor_teste}")