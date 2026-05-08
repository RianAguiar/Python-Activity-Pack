qtd = int(input("Quantidade de sensores: "))

normal = 0
atencao = 0
alerta = 0
evacuacao = 0

for i in range(qtd):
    nivel = float(input(f"Nível do sensor {i+1}: "))

    if nivel <= 2:
        normal += 1
    elif nivel <= 4:
        atencao += 1
    elif nivel <= 6:
        alerta += 1
    else:
        evacuacao += 1

print(f"Normal: {normal}")
print(f"Atenção: {atencao}")
print(f"Alerta: {alerta}")
print(f"Evacuação imediata: {evacuacao}")