import pyNizStek
class prosireniStek(pyNizStek.NizStek):
    def dodajMini(self):
        maks=self.Niz[0]
        for i in range(1, self.duzina()):
            if(self.Niz[i]>maks):
                maks=self.Niz[i]
        trecina=int(maks/3)
        print(f"Najveci broj je {maks} njegova trecina je {trecina}")
        if (self.jeLiPun()):
            print(f"STEK JE PUN! Ne mozemo dodati {trecina}")
            return
        self.dodajNaStek(trecina)
        self.prikazi()
