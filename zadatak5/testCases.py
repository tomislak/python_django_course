from zaposlenik import Zaposlenik, Poduzece, ErrZap, Student
import unittest

class TestPoduzece(unittest.TestCase):
    def test1(self):
        z1 = Zaposlenik("Ana Anic", 10000)
        z2 = Zaposlenik("Branko Brankic", 8900)
        z3 = Zaposlenik("Cvjetko Cvjetkic", 7500)
        p = Poduzece("ETK", "ZG")
        p.dodaj_zaposlenika(z1)
        p.dodaj_zaposlenika(z2)
        p.dodaj_zaposlenika(z3)
        self.assertEqual(len(p.zaposlenici), 3)
        p.izbaci_zaposlenika("Branko", "Brankic")
        self.assertEqual(len(p.zaposlenici), 2)
        with self.assertRaises(ErrZap):
            p.izbaci_zaposlenika("Branko", "Brankic")
        with self.assertRaises(ErrZap):
            p.dodaj_zaposlenika(z1)

    def test_student(self):
        s1 = Student("A B", 3500)
        self.assertEqual(s1.porez(), 350)

if __name__ == "__main__":
    unittest.main()
