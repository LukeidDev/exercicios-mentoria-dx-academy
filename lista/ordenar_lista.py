from get_list import get_list_random

def lista_ordenada():
    numeros = [get_list_random()]

    numeros_int = map(int, numeros)
    numeros_ordenados = sorted(numeros_int)
    print(numeros_ordenados)

lista_ordenada()