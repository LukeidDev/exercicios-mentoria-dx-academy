from calculadora.dig_num import input_numero1, input_numero2, input_operador

def operacoes():
    numero1 = input_numero1()
    operador = input_operador()
    numero2 = input_numero2()
    resultado = float

    if (operador == "+"):
        resultado = numero1 + numero2
    elif (operador == "-"):
        resultado = numero1 - numero2
    elif(operador == "*"):
        resultado = numero1*numero2
    elif(operador == "/"):
        resultado = numero1/numero2
    else:
        print("operador incorreto, tente novamente")
    
    print("O resultado é %.1f" % resultado)

    

    
