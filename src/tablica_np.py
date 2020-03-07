import numpy as np

def prosta():
    print()
    tablica = np.array([4,5,6])
    print("Tablica jednowymiarowa ", tablica)

    print()
    tablica_dwu = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("Tablica  dwuwymiarowa:\n", tablica_dwu)

    print()
    tablica_m = np.array([[1, 2, 3], ["raz", "dwa", "trzy"]])
    print("Tablica  dwuwymiarowa:\n", tablica_m)

    print()
    print("Rozmiat tablicy:")
    print("jednowymiarowa:", tablica.shape)
    print("jednowymiarowa:", tablica_dwu.shape)

def wybierz_elem (wiersz = 0, kolumna = 0):
    print()
    tablica = np.array([[1,2,3,4,5],[6,7,8,9,0]])

    x = tablica.shape
    # print("Kształt tablicy", x)
    print("Tablica:\n", tablica)

    print()
    print("Konkretna liczna z tablicy (0,0)- ", tablica[wiersz, kolumna])

    print("Podaj wiersz i kolume tablica o rozmiarze:", x)
    wiersz = int(input("P wiersz: "))
    kolumna = int(input("P kolumna: "))

    print("Wybrałeś:", tablica[wiersz, kolumna])

def wybierz_wk():
    tablica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Tab 3x3\n", tablica)

    print()
    print("Wiersz nr 1", tablica[0, :])
    print("Kolumna nr 3", tablica[:, 2])

# def losowanie():
#     tablica = np.random.rand()
#     print()
#     print("wYLOSOWANA TABLICA\n", tablica")

def zamien():
    tab_1_wym = np.zeros(3)
    tab_2_wym = np.zeros((5, 5))
    tabnn = np.zeros((2,2,2,2))
    print()
    print("Tablica jedno:\n", tab_1_wym)
    print("Tablica dwu:\n", tab_2_wym)
    # print("Tablica nn:\n", tabnn)

    a = 5
    tab_2_wym[2,3] = a
    print()
    print(tab_2_wym)
