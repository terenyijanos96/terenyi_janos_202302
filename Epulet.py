class Epulet:

    def __init__(self, sor):
        self.__nev = sor[0]
        self.__varos = sor[1]
        self.__orszag = sor[2]
        self.__magassag = float(sor[3].replace(",", "."))
        self.__emeletek_szama = int(sor[4])
        self.__epules_eve = int(sor[5])

    def __str__(self):
        return f"{self.__nev}, {self.__varos}, {self.__orszag}, {self.__magassag}, {self.__emeletek_szama}, {self.__epules_eve}"

    def get_nev(self):
        return self.__nev
    def get_varos(self):
        return self.__varos
    def get_orszag(self):
        return self.__orszag
    def get_magassag(self):
        return self.__magassag
    def get_emeletek_szama(self):
        return self.__emeletek_szama
    def get_epules_eve(self):
        return self.__epules_eve