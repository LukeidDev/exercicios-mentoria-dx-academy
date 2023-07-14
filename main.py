import time
from imc.calculo_imc import calcular_imc
from salario.calculo_salario import calcular_salario
from calculadora.funcoes_calculadora import operacoes
from escolha import escolha, retornar

escolha = escolha()

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