from abc import abstractmethod


class Zwierze:

@abstractmethod
    def daj_glos(self):
        raise NotImplementedError

    def idz_spac(self):
        print("Poszedłem spać")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam w oceanie")

class Lew(Zwierze):
    def daj_glos(self):
        print("Rawrr")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam na sawannie")

class Delfin(Zwierze):
    def daj_glos(self):
        print("......")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam w oceanie")

class Pies(Zwierze):
    def daj_glos(self):
        print("Hau hau")

    def powiedz_mi_gdzie_mieszkasz(self):
        print("Mieszkam w domu na ziemi.")

pies = Pies()
delfin = Delfin()
lew = Lew()
lew.daj_glos()
pies.daj_glos()
delfin.daj_glos()


