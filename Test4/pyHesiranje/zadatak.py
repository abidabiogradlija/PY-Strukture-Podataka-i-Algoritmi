import pyHash
class prosirenipyHash(pyHash.LinearniHash):
    def pronadiMin(self):
        min=self.Elementi[0]
        for i in range(1, self.velicina):
            if (self.Elementi[i]<min):
                min=self.Elementi[i]
        print(f"Najmanji broj je {min}")
        return min
    def izbaciElemente(self):
        j=0
        br=0
        while (j<len(self.Elementi)):
            if (self.Elementi[j] is not None):
                br+=1
            j+=1
        if (br==0):
            print("PRAZAN HASH")
            return

        minimalni=self.pronadiMin()
        for i in range(0, self.velicina):
            if (self.Elementi[i] == minimalni):
                self.Elementi[i]=self.praznoMjesto
        print("IZBACIVANJE IZVRSENO")
        self.prikazi()

