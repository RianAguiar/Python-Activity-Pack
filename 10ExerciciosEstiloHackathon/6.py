mensagem = input("Digite a mensagem: ").lower()

suspeitas = ["senha", "urgente", "clique", "prêmio", "pix", "bloqueado"]

contador = 0

for palavra in suspeitas:
    if palavra in mensagem:
        contador += 1

print(f"Palavras suspeitas encontradas: {contador}")

if contador == 0:
    print("Classificação: Mensagem normal")
elif contador <= 2:
    print("Classificação: Mensagem suspeita")
else:
    print("Classificação: Possível golpe")