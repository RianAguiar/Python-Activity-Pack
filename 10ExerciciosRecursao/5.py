def inverter_string(t):
    if t == "":
        return t
    return inverter_string(t[1:]) + t[0]
t = input("Digite uma string: ")
print(inverter_string(t))
