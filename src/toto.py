# 1. importujemy rand -> tworzymy funkcję losowanie -> wywołujemy ją w main
# 2. tworzymy funkcję lotek:
    # tworzymy listę i FORa dla listy -> wywołujemy w main
    # importujemy numpy -> instalujemy przez PIP -> tworzymy tablice

import random
import numpy as np

def losowanie ():
    liczba = random.randint(1, 10)
    print("wylosowana liczba = ", liczba)

def lotek(x=6):
    lista = []
    tablica = np.array

    for i in range(x):
        liczba = random.randint(1,49)
        print(i+1, liczba)
        # lista.append(liczba) #Dodawanie do listy
        """Do tablicy tablica dodajemy liczbe"""
        tablica = np.append(tablica, liczba)

    """Może się trafić, że liczby bądą się powtarzać dlatego jeśli starczy nam czasu"""
    """Możemy dodać IFa, który będzie nam sprawdzał czy liczba się powtórzyła i wtedy jeszcze raz będzie randomować"""
    # print("Szczęśliwe numery to: ", *lista)
    print("Szczęsliwe liczby tabliy", tablica)

