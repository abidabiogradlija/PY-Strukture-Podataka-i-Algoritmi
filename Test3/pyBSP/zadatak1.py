import pyBSP

class prosireniBSP(pyBSP.BSP):
    def arSredina(self, cvor):
        if self.korijen is None:
            print(f"Stablo je prazno!")
            return

        if cvor is None:
            return 0

        sum = int(cvor.element) + int(self.arSredina(cvor.lijevo)) + int(
            self.arSredina(cvor.desno))

        if cvor != self.korijen:
            return sum
        #-------------------------------OK



        print(f"Suma je {sum}")
        return sum


