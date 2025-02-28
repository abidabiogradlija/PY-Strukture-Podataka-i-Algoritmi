
import ctypes

class OtvorenoAdresiranje():

    def kreiraj_niz(self, k):
        return (ctypes.py_object * k)()
    
    def __init__(self, velicina, praznoMjesto):
        self.velicina = velicina                           
        self.Elementi = self.kreiraj_niz(self.velicina)   
        self.praznoMjesto = praznoMjesto                  

        for i in range(0, self.velicina):                 
            self.Elementi[i] = self.praznoMjesto
  
    def umetniHash(self, x):
        j = int(0)
        i = int(0)

        while True:
            j = self.hashFunkcija(x,i)    
            if self.Elementi[j] == self.praznoMjesto:
                self.Elementi[j] = x
                return True
            else:
                i = i + 1                
            if i >= self.velicina:
                break

        return False        

    def traziHash(self, x):
        i = 0       

        while True:
            index = self.hashFunkcija(x,i)       
            if(self.Elementi[index] == x):
                return index
            else:
                i = i + 1
            if self.Elementi[index] == self.praznoMjesto and i == self.velicina:
                break
        return self.praznoMjesto


    def prikazi(self):
        for i in range(0, self.velicina):
            print( str(i) + ": " + str(self.Elementi[i]))


    # UNZE PTF ASP 2021/2022 :: M.S. :: 19.01.2022