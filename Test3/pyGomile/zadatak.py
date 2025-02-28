import pyGomile

class prosirenaPyGomila(pyGomile.Gomila):
    def KubSume(self):
        if(self.velicina == 0):
            print("Gomila je prazna!")
            return
        sum = 0
        for i in range(0, self.velicina):
            sum += self.elementi[i]
        sum = sum ** 3
        print(f"Kub sume elemenata gomile: {sum}")

    def dajMin(self):   # Ovo nije rečeno u labovima, ali se često radi slično, pa evo i ovdje
        if (self.velicina == 0):
            print("Gomila je prazna!")
            return

        min = self.elementi[0]
        for i in range(0, self.velicina-1):
            if(min > self.elementi[i+1]):
                min = self.elementi[i+1]
        print(f"Minimalni element u gomili je: {int(min)}")