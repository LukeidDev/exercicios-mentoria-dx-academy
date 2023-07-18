from calculadora.dig_num import *
from calculadora.operadores import *

def operacoes():
    print("Digite a opção requisitada")
    print("1 - soma")
    print("2 - subtracao")
    print("3 - divisao")
    print("4 - multiplicação")
    print("5 - inteiro para binário")
    print("6 - raiz quadrada")
    print("7 - raiz cubica")

    select = int(input("Digite a opção: "))

    if(select == 5 or 6 or 7):
        c = input_numero3()
        resultado = int
    else:
        a = input_numero1()
        b = input_numero2()
        resultado = float



    if(select == 1):
        resultado = soma(a, b)
    elif(select == 2):
        resultado = subtracao(a, b)
    elif(select == 3):
        resultado = divisao(a, b)
    elif (select == 4):
        resultado = multiplicacao(a, b)
    elif(select == 5):
        resultado = int_for_bin(c)
    elif(select == 6):
        resultado = int_for_raiz(c)
    elif(select == 7):
        resultado = raiz_cubica(c)
    else:
        print("operador incorreto, tente novamente")

    if(select == 5):
        print("O resultado é {resultado}".format(resultado=resultado))
    else:
        print("O resultado é %.1f" % resultado)

    

    
