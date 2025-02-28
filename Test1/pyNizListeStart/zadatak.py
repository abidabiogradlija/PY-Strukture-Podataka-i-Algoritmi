import pyNizListe
class prosirenapyNizLista(pyNizListe.NizLista):
    def kvadratSume(self):
        suma=0
        for i in range(0, self.duzina):
            suma+=self.Niz[i]
        kvSume=suma ** 2
        print("Kvadrat suma =", kvSume)