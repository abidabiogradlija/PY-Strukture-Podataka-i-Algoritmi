import pyJPStek
class prosirenipyJPStek(pyJPStek.JPStek):
    def dajMax(self):
        max=self.vrh.element
        temp=self.vrh
        while(temp!=None):
            if(temp.element>max):
                max=temp.element
            temp=temp.sljedeci
        print(f"Najveci je {max}")



