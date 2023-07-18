import time
from imc.calculo_imc import calcular_imc
from salario.calculo_salario import calcular_salario
from calculadora.funcoes_calculadora import operacoes


def escolha():
    print("Escolha uma opção para prosseguir")
    print("1 - calculadora de imc")
    print("2 - calculador de salario mensal")
    print("3 - calculadora básica")

    escolha = int(input("Digite o valor escolhido: "))
    print("----------------------------------------------")

    if(escolha == 1):
        calcular_imc()
        retornar()
    elif(escolha == 2):
        calcular_salario()
        retornar()
    elif(escolha == 3):
        operacoes()
        retornar()
    else:
        escolha()

    return escolha

def retornar():

    print("Digite 'home' para retornar ao menu de escolha")
    retorno = str(input())

    if (retorno == "home"):
        escolha()
    else:
        time.sleep(1)