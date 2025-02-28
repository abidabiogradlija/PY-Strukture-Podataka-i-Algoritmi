import pyOtvorenoAdresiranje

class LinearniHash(pyOtvorenoAdresiranje.OtvorenoAdresiranje):

    def hashFunkcija(self, x ,i):
        return (x % self.velicina + i) % self.velicina


class DvostrukiHash(pyOtvorenoAdresiranje.OtvorenoAdresiranje):

    def hashFunkcija(self, x, i):
        return (x % self.velicina + i * (1 + x % (self.velicina - 2))) % self.velicina

# UNZE PTF ASP 2021/2022 :: M.S. :: 19.01.2022