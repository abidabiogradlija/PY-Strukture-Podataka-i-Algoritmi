import pyJPListe
class prosirenapyJPLista(pyJPListe.JPlista):
    def prebrojVece(self):
        brojac=0
        pocetni=self.pocetak.element
        i=self.pocetak
        i=i.sljedeci
        while (i != None):
            if (i.element>pocetni):
                brojac+=1
            i=i.sljedeci
        print(f"Brojac je {brojac}")
