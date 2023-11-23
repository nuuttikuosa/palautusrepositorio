import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.side_effect = [42, 43, 44]

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 7
            if tuote_id == 3:
                return 20
            if tuote_id == 4:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 2)
            if tuote_id == 3:
                return Tuote(3, "olut", 10)
            if tuote_id == 4:
                return Tuote(4, "kakku", 13)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, viitegeneraattori_mock)
    
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_attribuuteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla attribuuteilla
        # maidon hinta on 5, nimi on Pekka, pekan tilinumero 12345 ja viitteeksi on asetettu 42 ja 
        # kaupan tili on "33333-44455"
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_attribuuteilla_kaksi_eri_ostosta(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
            
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 7)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_attribuuteilla_kaksi_samaa_ostosta(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("tero", "54321")
        
            
        self.pankki_mock.tilisiirto.assert_called_with("tero", 42, "54321", "33333-44455", 20)

    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_attribuuteilla_kaksi_eri_ostosta_toista_ei_varastossa(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.lisaa_koriin(4)
        self.kauppa.tilimaksu("tero", "54321")
        
            
        self.pankki_mock.tilisiirto.assert_called_with("tero", 42, "54321", "33333-44455", 10)
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_attribuuteilla_kaksi_samaa_ostosta_ostoskori_nollataan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("tero", "54321")
        
            
        self.pankki_mock.tilisiirto.assert_called_with("tero", 42, "54321", "33333-44455", 10)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_viitenumerolla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("tero", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("tero", 42, "54321", ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("tero", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("tero", 43, "54321", ANY, ANY)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pasi", "6579")
        self.pankki_mock.tilisiirto.assert_called_with("pasi", 44, "6579", ANY, ANY)


    def test_poista_tuote_ostoskorista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pasi", "6579")
        self.pankki_mock.tilisiirto.assert_called_with("pasi", 42, "6579", ANY, 5)

        ## Kurssimateriaalissa sanottiin, että jos bugeja löytyy, korjaa ne. ostoskorista voi poistaa tuotteita vaikka niitä ei ole sillä ja samalla palautuvat varastoon
        ## tämä on varmaan bugi, mutta en tohtinut lisätä metodia jolla voisi tarkistaa ostoskorin sisällön. 
