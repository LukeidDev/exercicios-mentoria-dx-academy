from salario.dig_salario import dig_salario, bonus_salario, desconto_salario
from calculadora.operadores import soma, subtracao

def calcular_salario():
    
    print("Selecione uma operação")
    print("1 - calcular salario total com bonificação")
    print("2 - calcular salario total com desconto")

    select = int(input("Digite o valor selecionado: "))
    numero1 = dig_salario()
    result = float

    if (select == 1):
        numero2 = bonus_salario()

        result = soma(numero1, numero2)
        
        print("O salário total ao final será de : %.2f" % result)

    elif(select == 2):
        numero2 = desconto_salario()

        result = subtracao(numero1, numero2)
        print("O salário total ao final será de : %.2f" % result)
    
    else:
        print("valor de operação incorreto")

            

