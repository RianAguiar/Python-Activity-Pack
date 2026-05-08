total = 0

for i in range(7):
    consumo = float(input(f"Consumo do dia {i+1}: "))
    total += consumo

media = total / 7

print(f"Total semanal: {total:.2f} kWh")
print(f"Média diária: {media:.2f} kWh")

if media <= 10:
    print("Classificação: Consumo baixo")
elif media <= 20:
    print("Classificação: Consumo médio")
else:
    print("Classificação: Consumo alto")