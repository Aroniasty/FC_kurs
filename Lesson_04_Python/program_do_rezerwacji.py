rzad_1_miejsce_1 = False
rzad_1_miejsce_2 = False
rzad_1_miejsce_3 = False
rzad_1_miejsce_4 = False
rzad_1_miejsce_5 = False
rzad_1_miejsce_6 = False
rzad_1_miejsce_7 = False
rzad_1_miejsce_8 = False
rzad_2_miejsce_1 = False
rzad_2_miejsce_2 = False
rzad_2_miejsce_3 = False
rzad_2_miejsce_4 = False
rzad_2_miejsce_5 = False
rzad_2_miejsce_6 = False
rzad_2_miejsce_7 = False
rzad_2_miejsce_8 = False
# rzad_3_miejsce_1 = False
# rzad_3_miejsce_2 = False
# rzad_3_miejsce_3 = False
# rzad_3_miejsce_4 = False
# rzad_3_miejsce_5 = False
# rzad_3_miejsce_6 = False
# rzad_3_miejsce_7 = False
# rzad_3_miejsce_8 = False

'''
Napisz program do zarządzania rezerwacją miejsc w kinie.
Kino ma okresloną liczbę rzędów i miejsc w każdym rzedzie.
Twoim zadaniem jest stworzyć program, który umożliwia rezerwację miejsc dla widzów.
Każde miejsce może być zarezerwowane tylko raz, a każdy widz może zarezerwować maksymalnie jedno miejsce.

Program powinien umożliwić dodawanie rezerwacji dla kolejnych widzów, aż do wyczerpania dostępnych miejsc lub do momentu,
gdy użytkownik zdecyduje się zakończyć rezerwację (np. poprzez wprowadzenie specjalnej komendy).
/0 w paczkach

Jeśli próba zarezerwowania miejsca nie jest możliwa (np. miejsce jest już zajęte, nie istnieje, lub numer miejsca jest nieprawidłowy),
program powinien wyświetlić odpowiednią wiadomość o błędzie i kontynować rezerwację. # tutaj będzie coś innego niż w paczkach

Po zakończeniu rezerwacji program powinien wyświetlić następujące informacje:

    Liczbę zarezerwowanych miejsc
    Procent dostępnych miejsc, ktore zostały zarezerwowane
    Numer rzędu, w którym jest najwięcęcej zarezerwowanych miejsc
    Liczbę zarezerwowanych miejsc w tym rzędzie

Program powiinień również obsługiwać błędy, takie jak próba zarezerowania nieprawidłowego numeru miejsca lub próba rezerwacji,
gdy nie ma już dostępnych miejsc.

od użutkownika:
numer miejsca, które chce zarezerwować

co powinniśmy trzymać w naszym globalnym stanie
- ilość miejsc na sali oraz stan poszczególnych miejsc (czy są sprzedane?)
- ilość miejsc już sprzedanych
- ilość miejsc sprzedanych w danym rzedzie
- ilość rzędów
'''

print("Witaj w naszym systemie rezerwacji/sprzedży biletów")

ilosc_miejsc = 16
ilosc_rzedow = 2
ilosc_miejsc_sprzedanych_1_rzedzie = 0
ilosc_miejsc_sprzedanych_2_rzedzie = 0
#ilosc_miejsc_sprzedanych_3_rzedzie = 0

koniec_programu = False

while not koniec_programu:
    print("Podaj co chcesz zrobić w naszym programie.\n"
          "1. Zrób rezerwację miejsca\n"
          "2. Zakończ program i wyświetl nam potrzebne informacje.")
    wybor_menu = input("Wybierz opcję. ")
    if int(wybor_menu) == 1:
        rzad_uzytkownika = input("Podaj rząd, w którym chcesz zarezerwować miejsce ")
        if not int(rzad_uzytkownika) in range (1,3):
            print("Niestety nie mamy takiego rzędu w tym kinie.")
            continue
        miejsce_uzytkownika = input("Podaj miejsce ")
        if not int(miejsce_uzytkownika) in range(1,9):
            print("Niestety nie mamy takiego miejsca.")
            continue
        if int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 1:
            if not rzad_1_miejsce_1:
                rzad_1_miejsce_1 = True
                #ilosc_miejsc_sprzedanych += 1
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
                continue
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 2:
            if not rzad_1_miejsce_2:
                rzad_1_miejsce_2 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 3:
            if not rzad_1_miejsce_3:
                rzad_1_miejsce_3 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 4:
            if not rzad_1_miejsce_4:
                rzad_1_miejsce_4 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 5:
            if not rzad_1_miejsce_5:
                rzad_1_miejsce_5 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 6:
            if not rzad_1_miejsce_6:
                rzad_1_miejsce_6 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 7:
            if not rzad_1_miejsce_7:
                rzad_1_miejsce_7 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 1 and int(miejsce_uzytkownika) == 8:
            if not rzad_1_miejsce_8:
                rzad_1_miejsce_8 = True
                ilosc_miejsc_sprzedanych_1_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 1:
            if not rzad_2_miejsce_1:
                rzad_2_miejsce_1 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 2:
            if not rzad_2_miejsce_2:
                rzad_2_miejsce_2 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 3:
            if not rzad_2_miejsce_3:
                rzad_2_miejsce_3 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 4:
            if not rzad_2_miejsce_4:
                rzad_2_miejsce_4 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 5:
            if not rzad_2_miejsce_5:
                rzad_2_miejsce_5 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 6:
            if not rzad_2_miejsce_6:
                rzad_2_miejsce_6 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        elif int(rzad_uzytkownika) == 2 and int(miejsce_uzytkownika) == 7:
            if not rzad_2_miejsce_7:
                rzad_2_miejsce_7 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
        else:
            if not rzad_2_miejsce_8:
                rzad_2_miejsce_8 = True
                ilosc_miejsc_sprzedanych_2_rzedzie += 1
            else:
                print("Niestety, to miejsce jest już zajęte.")
    elif int(wybor_menu) == 2:
        koniec_programu = True
print("Zakończyliśmy działanie programu! Oto statystyki z Twojej sprzedaży: ")
print(f"Ilość sprzedanych biletów to: {ilosc_miejsc_sprzedanych_1_rzedzie + ilosc_miejsc_sprzedanych_2_rzedzie}")
print(f"Procentowo jest to: {((ilosc_miejsc_sprzedanych_1_rzedzie + ilosc_miejsc_sprzedanych_2_rzedzie)/ilosc_miejsc) * 100}")
#for rzad in ilosc_rzedow
if ilosc_miejsc_sprzedanych_1_rzedzie > ilosc_miejsc_sprzedanych_2_rzedzie:
    print(f"Najwięcej miejsc sprzedanych w 1 rzędzie. Było to: {ilosc_miejsc_sprzedanych_1_rzedzie} biletów")
elif ilosc_miejsc_sprzedanych_2_rzedzie > ilosc_miejsc_sprzedanych_1_rzedzie:
    print(f"Najwięcej miejsc sprzedanych w 2 rzędzie. Było to: {ilosc_miejsc_sprzedanych_2_rzedzie} biletów")
else:
    print(f"Sprzedaliśmy po tyle samo biletów w obydwu rzędach. Było to: {ilosc_miejsc_sprzedanych_1_rzedzie} biletów")