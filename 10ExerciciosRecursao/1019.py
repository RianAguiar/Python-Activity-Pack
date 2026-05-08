horas = 0
minutos = 0
segundos = 0
segundos = int(input('')) 

if segundos >= 60:
    minutos = segundos // 60
    segundos = segundos % 60

if minutos >= 60:
    horas = minutos // 60
    minutos = minutos % 60

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")