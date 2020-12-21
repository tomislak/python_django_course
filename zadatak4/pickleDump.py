from zaposlenik import *
import pickle

p = Poduzece("ETK", "Zagreb")
ana = Student("Ana Anic", 9000)
branko = Zaposlenik("Branko Brankic", 10000)
p.dodaj_zaposlenika(ana)
p.dodaj_zaposlenika(branko)

with open('pickletest.txt', 'wb') as fajl:
    pickle.dump(p, fajl)

print(pi)
