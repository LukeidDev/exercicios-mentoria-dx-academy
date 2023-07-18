from imc.dig_dados import dig_altura, dig_peso
from calculadora.operadores import multiplicacao, divisao

def calcular_imc():

    print("------------------------------------------")
    a = dig_peso()
    b = dig_altura()

    imc = divisao(a, multiplicacao(b, b))


    if (imc < 16.0):
        print("Seu imc é : %.1f, classificado como magreza grave" % imc)
    elif(imc >= 16.0 and imc <= 17):
        print("Seu imc é %.1f, classificado como magreza moderada" % imc)
    elif(imc >= 17.0 and imc <= 18.5):
        print("Seu imc é %.1f, classificado como magreza leve" % imc)
    elif(imc >= 18.5 and imc <= 24,9):
        print("Seu imc é : %.1f, classificado como Saudável" % imc)
    elif(imc >= 25.0 and imc <= 29,9):
        print("Seu imc é : %.1f, classificado como sobrepeso" % imc)
    elif(imc >=30.0 and imc <= 39,9):
        print("Seu imc é : %.1f, classificado como obesidade" % imc)
    elif(imc >40.0):
        print("Seu imc é : %.1f, classificado como obesidade grave" % imc)

    print("----------------------------------------------")
    