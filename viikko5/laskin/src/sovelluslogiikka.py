class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        


    
    def suorita(self):
        try:
            operandi =  int(self._lue_syote())
        except Exception:
            pass
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.arvo() + operandi)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
    
    def suorita(self):

        try:
            operandi =  int(self._lue_syote())
        except Exception:
            pass
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.arvo() - operandi)

class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
    
    
    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(0)


class Kumoa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
    
    
    def suorita(self):
        self.sovelluslogiikka.kumoa()


class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvot = []
        self._arvot.append(arvo)

   # def miinus(self, operandi):
    #    self._arvo = self._arvo - operandi

    #def plus(self, operandi):
    #    self._arvo = self._arvo + operandi

    #def nollaa(self):
    #    self._arvo = 0
    def kumoa(self):
        self._arvot.pop()

    def historia(self):
        return len(self._arvot)
    
    def aseta_arvo(self, arvo):
        self._arvot.append(arvo)

    def arvo(self):
        return self._arvot[-1]
