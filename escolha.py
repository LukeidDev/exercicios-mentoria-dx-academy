
import time


def escolha():
    print("Escolha uma opção para prosseguir")
    print("1 - calculadora de imc")
    print("2 - calculador de salario mensal")
    print("3 - calculadora básica")

    escolha = int(input("Digite o valor escolhido: "))
    print("----------------------------------------------")

    return escolha

def retornar():

    print("Digite 'home' para retornar ao menu de escolha")
    retorno = str(input())

    if (retorno == "home"):
        escolha()
    else:
        time.sleep(1)