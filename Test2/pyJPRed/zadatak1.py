import pyJPRed

class prosireniPyJPRed(pyJPRed.JPRed):

    def ariSredina(self):
        if(self.jeLiPrazan()):
            print("Red je prazan!")
            return
        sum = 0
        temp = self.pocetak
        while temp is not None:
            sum += int(temp.element)
            temp = temp.sljedeci
        ariSredina = sum / float(self.duzina())
        print(f"Aritmeticka sredina svih elemenat u strukturi je: {ariSredina}")

    def dajMinimum(self):
        if(self.jeLiPrazan()):
            print("Red je prazan!")
            return
        minimum = self.pocetak.element
        temp = self.pocetak
        while temp is not None:
            if(int(minimum) > int(temp.element)):
                minimum = int(temp.element)
            temp = temp.sljedeci
        print(f"Najmanji element u strukturi je: {minimum}")