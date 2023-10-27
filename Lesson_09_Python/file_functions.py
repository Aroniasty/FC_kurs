# file = open("uczniowie.txt")
# # print(file.read())
# # print(file.readline())
# # print(file.readlines())
# for linijka in file:
#     print(linijka)
# file.close()

# with open(file="uczniowie.txt", mode="r+") as file2: #"r" - odczyt, "r+" - odczyt/zapis, "a" - zapis na końcu pliku, "a+" czytanie, zapis i kursor na końcu pliku
#     file2.write("Podpisał Michal Zietkowski")
#     for linijka in file2:
#         print(linijka)
#     file2.write("Nowy podpis")
#
# with open(file="uczniowie.txt", mode="w+") as file2: # zastąpi plik nowym wpisem
#     for line in file2:
#         print(line)
#     file2.write("Nowy podpis2")



# context manager
class OtworzPiwo():
    def __enter__(self):
        print("Otworzyłem piwo")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Zamknij piwo")

# with OtworzPiwo() as piwo:
#     print(piwo)
#     print("Pijemy piwko")

with open("slowniki.txt", mode="a+") as new_file:
    new_file.write("raz dwa trzy")
    for line in new_file:
        print(line)