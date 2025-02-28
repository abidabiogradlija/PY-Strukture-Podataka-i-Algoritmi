import pyBSP
class prosirenipyBSP(pyBSP.BSP):
    def minimalniElement(self):
        if(self.korijen==None):
            print("STABLO PRAZNO")
            return
        temp = self.korijen
        while (temp.lijevo != None):
            temp = temp.lijevo
        minimalni=temp.element
        print(f"Minimalni je {minimalni}")
        novi=int(minimalni)+1
        self.umetniIterativno(novi)
        print(f"Umetnut je broj {novi} iterativno")
    def sumaFunkcija(self, korijen):
        if korijen is None:
            return 0
        suma=korijen.element + self.sumaFunkcija(korijen.lijevo) + self.sumaFunkcija(korijen.desno)
        return suma
    def brojacElemenata(self, korijen):
        if korijen is None:
            return 0
        brojac=1 + self.brojacElemenata(korijen.lijevo) + self.brojacElemenata(korijen.desno)
        return brojac

    def aritmetickaSr(self):
        sumaElemenata=int(self.sumaFunkcija(self.korijen))
        brojac=int(self.brojacElemenata(self.korijen))
        arSr=float(sumaElemenata/brojac)
        print(f"Suma elemenata je {sumaElemenata}")
        print(f"Brojac elemanata je {brojac}")
        print(f"Aritmeticka sredina je {arSr}")












