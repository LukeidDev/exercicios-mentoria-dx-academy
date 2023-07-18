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
    a = dig_salario()
    result = float

    if (select == 1):
        b = bonus_salario()

        result = soma(a, b)
        
        print("O salário total ao final será de : %.2f" % result)

    elif(select == 2):
        b = desconto_salario()

        result = subtracao(a, b)
        print("O salário total ao final será de : %.2f" % result)

    elif(select == 3):
        result = real_for_dolar(a)
        print("O salário total ao final será de : %.2f" % result)

    elif(select == 4):
        result = real_for_euro(a)
        print("O salário total ao final será de : %.2f" % result)
    elif(select == 5):
        result = real_for_yuan(a)
        print("O salário total ao final será de : %.2f" % result)

    
    else:
        result = dig_salario
    


            

