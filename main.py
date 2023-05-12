wyraz_ciagu = 1
wyraz_ciagu = int(wyraz_ciagu)
lista_wyrazow_ciagu = []
while True:
    liczba=input("Wpisz liczbe calkowita od 1 do 100:"  )
    liczba = int(liczba)
    if liczba < 1 or liczba > 100:
        print("Wpisales zla liczbe. Sproboj jeszcze raz")
        continue
    else:
        lista_wyrazow_ciagu.append(liczba)
        while True:
            if liczba % 2 == 0:
                liczba = liczba/2
                lista_wyrazow_ciagu.append(liczba)
                print("Liczba - {}".format(liczba))
                wyraz_ciagu = wyraz_ciagu +1
                print("Wyraz ciagu - {}".format(wyraz_ciagu))
            elif not liczba % 2 == 0:
                liczba = 3*liczba+1
                lista_wyrazow_ciagu.append(liczba)
                print("Liczba - {}".format(liczba))
                wyraz_ciagu = wyraz_ciagu + 1
                print("Wyraz ciagu - {}".format(wyraz_ciagu))
            if liczba == 1:
                print("Dlugosc ciagu wynosi {} wyrazow: {}".format(wyraz_ciagu, lista_wyrazow_ciagu))
                break
