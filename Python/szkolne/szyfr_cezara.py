petla = "tak"
while petla=="tak":
    ostateczne_slowo=[]
# Uzytkownik podaje przesuniecie liter
    przesuniecie = int(input("Wybierz przesuniecie w szyfrze: "))

# Uzytkownik wybiera, czy chce zaszyfrowac czy odszyfrowac informacje. Pyta do skutku.
    dzialanie = input("Chcesz zakodowac czy odkodowac jakas informacje? (zakodowac/odkodowac) ")
    while dzialanie!="zakodowac" and dzialanie!="odkodowac":
        dzialanie = input("Nie obsluguje takiej komendy. \nWybierz jeszcze raz: ")

#szyfrowanie --> funkcja
    def szyfrowanie(przesuniecie):
        slowo = input("Podaj slowo ktore chcesz zaszyfrowac: ")
        litery = list(slowo)


#tworzenie slownika zawierajacego afbabet
    alfabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
           "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
            "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26 }

#slownik pozwalajacy na odwrocenie kodu
    alfabet_odwrocony = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
                     11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s",
                     20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}

#Zrob przesuniecie key+przesuniecie
#Uzytkownik podaje slowo, przechodzimy po literach uzywajac list
    slowo = input("Podaj slowo: ")

    if dzialanie=="zakodowac":
        for litera in slowo:
            if alfabet[litera]+przesuniecie <=26:
                nowa = alfabet[litera]+przesuniecie
                ostateczne_slowo.append(alfabet_odwrocony[nowa])
            else:
                nowa = alfabet[litera]+przesuniecie-26
                ostateczne_slowo.append(alfabet_odwrocony[nowa])        
    else:
        for litera in slowo:
            if alfabet[litera]-przesuniecie > 0:
                nowa = alfabet[litera]-przesuniecie
                ostateczne_slowo.append(alfabet_odwrocony[nowa])
            else:
                nowa = 26-(0-(alfabet[litera]-przesuniecie))
                ostateczne_slowo.append(alfabet_odwrocony[nowa])

    print(ostateczne_slowo)
    petla=input("Jeszcze raz? (tak/nie) ")
    if petla!="tak":
        if petla!="nie":
            petla=input("Nie obsluguje takiej komendy. \nJeszcze raz? (tak/nie) ")