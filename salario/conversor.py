from calculadora.operadores import divisao

def real_for_dolar(numero1):
    return divisao(numero1, 4.81)

def real_for_euro(numero1):
    return divisao(numero1, 5.42)

def real_for_yuan(numero1):
    return divisao(numero1, 0.67)