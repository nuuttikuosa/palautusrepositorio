KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti


        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):

        if n in self.lukujono[:self.alkioiden_lkm]:
            return True
        return False

    def lisaa(self, n):


        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.lukujono):
                self.lukujono = self.lukujono + [0]*self.kasvatuskoko
                
            return True

        return False

    def poista(self, n):
        
        try:
            kohta = self.lukujono[:self.alkioiden_lkm].index(n)
        except Exception:
            return False
        
        for i in range(kohta,self.alkioiden_lkm -1 ):
            self.lukujono[i] = self.lukujono[i + 1]
        
        self.lukujono[self.alkioiden_lkm -1] = 0
        self.alkioiden_lkm -=  1
        
        return True
      
    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):    
        return self.lukujono[:self.alkioiden_lkm]
    
    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for i in (a.to_int_list()+b.to_int_list()):
            x.lisaa(i)
        return x
        

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()

        for i in a.to_int_list():
            if i in b.to_int_list():
                y.lisaa(i) 
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()

        for i in a.to_int_list():
            if i not in b.to_int_list():
                z.lisaa(i)
        return z

    def __str__(self):
        return f"\u007b{str(self.to_int_list())[1:-1]}\u007d"