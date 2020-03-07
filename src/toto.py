import random
import numpy as np

def losowanie ():
    liczba = random.randint(1, 10)
    print("Wylosowan liczba = ", liczba)

def lotek( x = 6 ):
    lista = []
    tablica = np.array

    for i in range(x):
        liczba = random.randint(1, 49)
        print(i+1, liczba)
        # lista.append(liczba)
        tablica = np.append(tablica, liczba)

    # print(lista)
    print("Szczęscliwe numery to: ", tablica)