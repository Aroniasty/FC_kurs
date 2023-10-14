import subprocess

# Run the other script
print("Witaj w naszym programie matematycznym")
print("Opcje, które możesz wykonać to: \n"
      "1. Dodawanie\n"
      "2. Odejmowanie")
opcja = input("Wybierz opcję: ")
pierwsza_liczba = input("podaj pierwszą liczbę: ")
druga_liczba = input("Podaj drugą liczbę: ")
subprocess.run(["python3", "skrypty.py", opcja, pierwsza_liczba, druga_liczba])