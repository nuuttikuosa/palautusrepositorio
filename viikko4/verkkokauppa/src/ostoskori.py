class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista_kaikki(self, tuote):
        self._tuotteet = list(
            filter(lambda t: t.id != tuote.id, self._tuotteet)
        )

    def poista(self, tuote):
        #korjattu poista funktio sellaiseksi että poistaa vain yhden kappaleen tuotteita, ei kaikkia,
        for i in range(len(self._tuotteet)):
            if tuote.id == self._tuotteet[i].id:
                del self._tuotteet[i]
                return

    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
