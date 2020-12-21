class Zaposlenik:
    def __init__(self, ime_i_prezime, placa):
        self.ime, self.prezime = ime_i_prezime.split()
        self.placa = placa

    def __str__(self):
        return "{} {}, {}".format(self.ime, self.prezime, self.placa)

    def daj_povisicu(self, postotak):
        self.placa = self.placa * (1 + postotak / 100)

    def porez(self):
        return 0.24 * self.placa

class Student(Zaposlenik):
    def porez(self):
        return 0.1 * self.placa

class Poduzece:
    def __init__(self, ime, lokacija ):
        self.ime = ime
        self.lokacija = lokacija
        self.zaposlenici = []

    def dodaj_zaposlenika(self, Zaposlenik):
        if Zaposlenik in self.zaposlenici:
            raise ErrZap("DOD", Zaposlenik.ime, Zaposlenik.prezime)
        self.zaposlenici.append(Zaposlenik)

    def povisi_svima(self, postotak):
        for zap in self.zaposlenici:
            zap.daj_povisicu(postotak)

    def porez(self):
        return sum(zap.porez() for zap in self.zaposlenici)

    def izbaci_zaposlenika(self, ime, prezime):
        for zap in self.zaposlenici:
            if zap.ime == ime and zap.prezime == prezime:
                self.zaposlenici.remove(zap)
                return
        raise ErrZap("IZB", ime, prezime)

    def __str__(self):
        s = "{}, {}\n".format(self.ime, self.lokacija)
        z = "\n".join([str(zap) for zap in self.zaposlenici])
        return s + z

    def __iter__(self):
        self.brojac = -1
        return self

    def __next__(self):
        self.brojac += 1
        if self.brojac == len(self.zaposlenici):
            raise StopIteration
        return self.zaposlenici[self.brojac]

class ErrZap(Exception):
    def __init__(self, tip, ime, prezime):
        self.tip = tip
        self.ime = ime
        self.prezime = prezime

    def __str__(self):
        if self.tip == "DOD":
            return 'Greska u dodavanju; {} {} vec postoji'.format(self.ime, self.prezime)
        if self.tip == "IZB":
            return 'Greska u izbacvanje; {} {} ne postoji'.format(self.ime, self.prezime)


if __name__ == '__main__':
    p = Poduzece("ETK", "Zagreb")
    ana = Student("Ana Anic", 9000)
    branko = Zaposlenik("Branko Brankic", 10000)
    p.dodaj_zaposlenika(ana)
    p.dodaj_zaposlenika(ana)
    p.dodaj_zaposlenika(branko)

    try:
        p.dodaj_zaposlenika(ana)
    except ErrZap as e:
        print(e)

    print(p)
    p.povisi_svima(10)
    for zaposlenik in p:
        print(zaposlenik)
    p.izbaci_zaposlenika('Ana', 'Anic')

    try:
        p.izbaci_zaposlenika('Miro', 'Miric')
    except ErrZap as e:
        print(e)

    print(p)
