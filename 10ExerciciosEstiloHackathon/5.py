distancia = float(input("Distância até o destino (km): "))
autonomia = float(input("Autonomia do drone (km): "))

distancia_total = distancia * 2

print(f"Distância total: {distancia_total:.2f} km")

if distancia_total <= autonomia:
    sobra = autonomia - distancia_total
    print("Entrega possível")
    print(f"Autonomia restante: {sobra:.2f} km")
else:
    falta = distancia_total - autonomia
    print("Entrega impossível")
    print(f"Faltam: {falta:.2f} km de autonomia")