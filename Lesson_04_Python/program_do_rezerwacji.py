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
rzad_3_miejsce_1 = False
rzad_3_miejsce_2 = False
rzad_3_miejsce_3 = False
rzad_3_miejsce_4 = False
rzad_3_miejsce_5 = False
rzad_3_miejsce_6 = False
rzad_3_miejsce_7 = False
rzad_3_miejsce_8 = False

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

ilosc_miejsc = 24
ilosc_rzedow = 3
ilosc_miejsc_sprzedanych_1_rzedzie = 0
ilosc_miejsc_sprzedanych_2_rzedzie = 0
ilosc_miejsc_sprzedanych_3_rzedzie = 0

koniec_programu = False

while not koniec_programu:

    rzad_uzytkownika = input("Podaj rząd, w którym chcesz zarezerwować miejsce ")
    if not int(rzad_uzytkownika) in range (1,4):
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