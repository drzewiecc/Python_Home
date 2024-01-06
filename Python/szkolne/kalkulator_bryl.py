import math
grac="tak"
def gra():
    print("Wybierz bryle, ktorej objetosc chcesz policzyc:")
    print("1 - szescian, 2 - prostopadloscian, 3 - ostroslup, 4 - stozek, 5 - walec, 6 - kula, 7 - graniastoslup")
    wybor = int(input("Podaj numer swojej bryly: "))
    if wybor==1:
        a = int(input("Podaj dlugosc krawedzi: "))
        print("Objetosc tego szescianu wynosi ", a*a*a, ".")
    elif wybor==2:
        a = int(input("Podaj dlugosc pierwszej krawedzi: "))
        b = int(input("Podaj dlugosc drugiej krawedzi: "))
        c = int(input("Podaj dlugosc trzeciej krawedzi: "))
        print("Objetosc tego prostopadloscianu wynosi ", a*b*c, ".")
    elif wybor==3:
        p = int(input("Podaj pole podstawy: "))
        h = int(input("Podaj wysokosc bryly: "))
        print("Objetosc tego ostroslupa wynosi ", p/3*h, ".")
    elif wybor==4:
        r = int(input("Podaj promien kola w podstawie: "))
        h = int(input("Podaj wysokosc bryly: "))
        print("Objetosc tego stozka wynosi ", h/3*r*r*math.pi, ".")
    elif wybor==5:
        r = int(input("Podaj promien kola w podstawie: "))
        h = int(input("Podaj wysokosc bryly: "))
        print("Objetosc tego walca wynosi ", h*r*r*math.pi, ".")
    elif wybor==6:
        r = int(input("Podaj promien bryly: "))
        print("Objetosc tej kuli wynosi ", 4/3*r*r*r*math.pi, ".")
    elif wybor==7:
        p = int(input("Podaj pole podstawy: "))
        h = int(input("Podaj wysokosc bryly: "))
        print("Objetosc tego graniastoslupa wynosi ", p*h, ".")

while grac=="tak":
    gra()
    grac=input("Jeszcze raz? (tak/nie) ")
    while grac!="tak" and grac!="nie":
        print("Nie obsluguje takiej komendy.")
        grac=input("Jeszcze raz? (tak/nie) ")