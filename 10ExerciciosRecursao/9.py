def decodificar(msg):
    print(msg)
    if len(msg) == 1:
        return
    decodificar(msg[1:])
decodificar("abc")