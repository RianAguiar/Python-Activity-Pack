pessoa = 45
quantidade_pessoas =  int(input("Digite o numero de pessoas na fila: "))
espera = (quantidade_pessoas * pessoa)/60
print(espera)
if espera < 5:
    print("Fila rapida")
elif espera >= 5 and espera <= 15:
    print("Fila moderada")
elif espera > 15:
    print("Fila demorada")
