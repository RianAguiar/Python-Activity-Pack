"essa questão foi feito com auxilio de IA pq n sabia a função capitalize"

qtd = int(input("Quantidade de coletas: "))

materiais = {
    "papel": 0,
    "plástico": 0,
    "vidro": 0,
    "metal": 0,
    "orgânico": 0
}

for i in range(qtd):
    tipo = input("Tipo de material: ").lower()
    peso = float(input("Peso em kg: "))

    if tipo in materiais:
        materiais[tipo] += peso

print("\nTotais:")

for material, total in materiais.items():
    print(f"{material.capitalize()}: {total:.2f} kg")

maior = max(materiais, key=materiais.get)

print(f"\nMaterial mais coletado: {maior.capitalize()}")