baza_szkolna = {
    "1a": [{
        "imie": "Michal",
        "nazwisko": "Zietkowski",
        "oceny": [1, 2, 4]
        },
        {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "oceny": [2, 3, 5]
        }
    ]
}

print("Witaj w programie do zarządzania naszą szkołą. Podaj co chcesz zrobić.")
wybor_uzytkownika = input("1. Dodaj ocenę uczniowi\n2. Dodaj ucznia\n3. Zmień wartość u ucznia\n")
if wybor_uzytkownika == "1":
    klasa_ucznia = input("Podaj klasę ucznia: ")
    imie_ucznia = input("Podaj imię ucznia: ")
    nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
    ocena_ucznia = input("Podaj ocenę ucznia: ")
    for numer_klasy, klasa in baza_szkolna.items():
        if klasa_ucznia == numer_klasy:
            for uczen in klasa:
                if imie_ucznia == uczen.get("imie") and nazwisko_ucznia == uczen.get("nazwisko"):
                    uczen["oceny"].append(int(ocena_ucznia))
                    break
                print("Nie ma takiego ucznia.")
elif wybor_uzytkownika == "2":
    klasa_ucznia = input("Podaj klasę ucznia: ")
    imie_ucznia = input("Podaj imię ucznia: ")
    nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
    for numer_klasy, klasa in baza_szkolna.items():
        baza_szkolna[klasa_ucznia] = {

        }

# 0:22:00