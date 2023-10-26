import sys

argumenty = sys.argv[1:]
koniec_programu = False
print("Witaj w naszej szkole, podaj opcję jaką chcesz wykonać.")

lita_uczniow = []

def znajdz_uzytkownika_w_nauczycielach(dane_uzytkownika):
    print("Kod do znalezienia danych z argumentow systemowych wsrod uczniow")

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

while not koniec_programu:
    wybrana_opcja = input("1. Dodaj Ucznia\n2. Dodaj nauczyciela\n3. Dodaj wychowawcę\n4. Koniec\n")
    if wybrana_opcja == "1":
        imie_input = input("Podaj imię ucznia: ")
        nazwisko_input = input("Podaj nazwisko ucznia: ")
        klas_input = input("Podaj Klasę ucznia: ")
        nowy_uczeni = Uczen(imie=imie_input, nazwisko=nazwisko_input, klasa=klas_input)
    elif wybrana_opcja == "2":
        print("Dodajemy nauczyciela")
        pusty_input = False
        while not pusty_input:
            numer_klasy = input("Podaj kolejną klasę: ")
            if numer_klasy == "":
                pusty_input = True
    elif wybrana_opcja == "3":
        print("Dodajemy wychowawce")
    elif wybrana_opcja == "4":
        print("koniec - wykonujemy operacje z argumentow systemowych")
        print(argumenty)
        koniec_programu = True