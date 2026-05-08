anos = 0
meses = 0 
dias = int(input(''))

if dias >= 365:
    anos = dias // 365
    dias = dias % 365
if dias >= 30:
    meses = dias // 30
    dias = dias % 30
if dias >= 30:
    dias = dias % 30
    meses = meses + 1

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")

