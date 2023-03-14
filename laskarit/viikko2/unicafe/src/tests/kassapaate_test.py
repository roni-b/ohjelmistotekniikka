import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_kassan_rahat(self):
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    
    def test_myydyt_lounaat(self):
        self.assertEqual(int(self.kassapaate.edulliset), 0)
        self.assertEqual(int(self.kassapaate.maukkaat), 0)
    
    def test_liian_vahan_kateista_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(int(self.kassapaate.maukkaat), 0)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    
    def test_liian_vahan_kateista_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(int(self.kassapaate.edulliset), 0)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_edullinen_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(int(self.kassapaate.edulliset), 1)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100240)
    
    def test_maukas_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(int(self.kassapaate.maukkaat), 1)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100400)

    def test_maukas_kortti(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(int(self.kassapaate.maukkaat), 1)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    
    def test_edullinen_kortti(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(int(self.kassapaate.edulliset), 1)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_liian_vahan_kortilla_maukas(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(int(self.kassapaate.maukkaat), 0)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)

    def test_liian_vahan_kortilla_edullinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(int(self.kassapaate.edulliset), 0)
        self.assertEqual(int(self.kassapaate.kassassa_rahaa), 100000)
    
    def test_rahan_lataus_kortille_onnistuu(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(int(kortti.saldo), 2000)

    def test_rahan_lataus_kortille_ei_onnistu(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1)
        self.assertEqual(int(kortti.saldo), 1000)