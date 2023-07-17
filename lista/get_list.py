import random

def get_list_random():

    random.seed()
    numeros = random.getstate()
    print(random.sample(range(10), k=5))
    return numeros

