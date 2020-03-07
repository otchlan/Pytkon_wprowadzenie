
def suma(a, b):
    print(a+b)

def jezeli (a, b ,c):
    ab = a + b
    if ab == c:
        print("if.1=", ab)
    elif a+c == b:
        print("if.2=", a+c)
    elif b+c == a:
        print("if.3=", b+c)
    else:
        print("żadna liczba nie pasuje")

def petla_while():
    x = 1
    while x < 5:
        print("Dalej x= ", x)
        x += 1

def petla_for():
    for x in range(2, 5):
        print(x)
