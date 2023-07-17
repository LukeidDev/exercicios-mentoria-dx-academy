from salario.dig_salario import dig_salario, bonus_salario, desconto_salario
from calculadora.operadores import soma, subtracao
from salario.conversor import real_for_dolar, real_for_euro, real_for_yuan

def calcular_salario():
    
    print("Selecione uma operação")
    print("1 - calcular salario total com bonificação")
    print("2 - calcular salario total com desconto")
    print("3 - conversor de real para dolar")
    print("4 - conversor de real para euro")
    print("5 - conversor de real para yuan")

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

    elif(select == 3):
        result = real_for_dolar(numero1)
        print("O salário total ao final será de : %.2f" % result)

    elif(select == 4):
        result = real_for_euro(numero1)
        print("O salário total ao final será de : %.2f" % result)
    elif(select == 5):
        result = real_for_yuan(numero1)
        print("O salário total ao final será de : %.2f" % result)

    
    else:
        result = dig_salario
    


            

