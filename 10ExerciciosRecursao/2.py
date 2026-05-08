lista_str = []
numeros = input("digite: ")
lista_str.append(numeros.split(","))
lista_int = [int(i) for i in lista_str]
print(lista_int)
def soma_lista(lista_int):
    if len(lista_int) == 0:
        return 0
    '''return lista[0] + soma_lista(lista[1:])'''
print(soma_lista(lista_int))