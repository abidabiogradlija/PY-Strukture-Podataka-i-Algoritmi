import pyPretrazivanja
class prosirenapyPretrazivanja(pyPretrazivanja.pyPretrazivanjeNizListe):
    def minElement(self):
        i=0
        min=self.Niz[0]
        while (i<self.duzina):
            if (self.Niz[i]<min):
                min=self.Niz[i]
            i = i + 1
        print(f"Najmanji broj je {min}")
        noviElement=int(min+1)
        self.dodaj(noviElement)
        print("USPJESNO DODAN NOVI ELEMENT:")
        self.prikazi()
