
def suma (a, b):
    print("w klasie", a+b)

def jezeli (a, b, c):

    ab = a+b
    if ab == c:
        print ("if-1 a+b=c", a+b)
    elif a+c == b:
        print ("if-2 a+c=b", a+c)
    elif b+c == a:
        print ("if-3 b+c=a", b+c)
    else:
        print ("żadna liczba nie psuje")

"""1.True"""
"""2.<"""
"""3.<="""
def petla_while ():
    x = 1
    while x <= 10:
        print("Lecimy dalej. x = ", x)
        x += 1

def petla_for ():
    for x in range(2, 5):
        print(x)

