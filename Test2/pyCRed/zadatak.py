import pyCRed
class prosirenipyCRed(pyCRed.CRed):
    def prebrojManje(self):
        if(self.jeLiPrazan()):
            print("PRAZAN")
            return
        brojac=0
        pocetni=self.pocetak
        i=self.pocetak
        while True:
            if(int(self.Niz[i])<int(self.Niz[pocetni])):
                brojac=brojac+1
            i=(i+1)%self.kapacitet
            if (i == (self.kraj + 1) % self.kapacitet):
                break
        print(f"Brojac= {brojac}")

