import unittest

# Devo importare la classe Veicolo, attualmente mi trovo in gestione_veicoli/test/testveicolo.py e la classe Veicolo si trova in gestione_veicoli/classes/veicolo.py
from classes.veicolo import Veicolo


class TestVeicolo(unittest.TestCase):
    def setUp(self):
        self.veicolo = Veicolo("AB123CD", "Fiat", "Panda", 5, 10000.0)

    def test_get_targa(self):
        self.assertEqual(self.veicolo.get_targa(), "AB123CD")

    def test_get_marca(self):
        self.assertEqual(self.veicolo.get_marca(), "Fiat")

    def test_get_modello(self):
        self.assertEqual(self.veicolo.get_modello(), "Panda")

    def test_get_numero_posti(self):
        self.assertEqual(self.veicolo.get_numero_posti(), 5)

    def test_get_prezzo_base(self):
        self.assertEqual(self.veicolo.get_prezzo_base(), 10000.0)

    def test_set_prezzo_base(self):
        self.veicolo.set_prezzo_base(15000.0)
        self.assertEqual(self.veicolo.get_prezzo_base(), 15000.0)

    def test_set_prezzo_base_invalid(self):
        with self.assertRaises(ValueError):
            self.veicolo.set_prezzo_base(-1000)


if __name__ == "__main__":
    unittest.main()
