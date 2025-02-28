
class Cvor:
    def __init__(self, element=None):
        self.element = element
        self.sljedeci = None
    
    def __str__(self):
        return str(self.element)

class JPlista():
    def __init__(self):
        self.pocetak = None
        self.kraj = None
        self.tekuci = None
        self.dduzina = 0
        self.lduzina = 0

    def idiNaPocetak(self):
        self.tekuci = self.pocetak
        self.dduzina += self.lduzina
        self.lduzina = 0
        print("Pokazivač tekući postavljen na POČETAK liste!")
    
    def idiNaKraj(self):
        self.tekuci = self.kraj
        self.lduzina += self.dduzina
        self.dduzina = 0
        print("Pokazivač tekući postavljen na KRAJ liste!")

    def idiNaSljedeci(self):
        if(self.dduzina != 0):
            if(self.tekuci == None):
                self.tekuci = self.pocetak
                print("Pokazivač je postavljen an POČETAK liste!")
            else:
                self.tekuci = self.tekuci.sljedeci
            self.lduzina += 1
            self.dduzina -= 1
            print("Pokazivač tekući postavljen na SLJEDEĆI ELEMENT liste!")
        else:
            print("Pokazivač tekući je na kraju liste!")

    def idiNaPrethodni(self):
        if(self.lduzina != 0):
            if(self.lduzina == 1):
                self.tekuci = self.pocetak
                print("Pokazivač je postavljen na POČETAK liste!")
            else:
                privremeni = self.pocetak
                while(privremeni.sljedeci != self.tekuci):
                    privremeni = privremeni.sljedeci
                self.tekuci = privremeni
                print("Pokazivač tekući je postavljen na PRETHODNI ELEMENT liste!")
            self.lduzina -= 1
            self.dduzina += 1
        else:
            print("Pokazivač tekući je na početku liste!")

    def idiNaPoziciju(self, pozicija):
        if((pozicija < 0) or (pozicija > (self.lduzina + self.dduzina))):
            print("Zadata pozicija je izvan raspona!")
        else:
            self.dduzina = self.dduzina + self.lduzina - pozicija
            self.lduzina = pozicija
            if(pozicija == 0):
                self.tekuci = self.pocetak
                print("Pokazivač tekući pokazuje na POČETAK liste")
            else:
                self.tekuci = self.pocetak
                for i in range(0,pozicija-1):
                    self.tekuci = self.tekuci.sljedeci
            print("Pokazivač tekući postavljen na poziciju:" + str(pozicija))

    def dodaj(self, x):
        novicvor = Cvor(x)
        
        if(self.dduzina+self.lduzina == 0):
            self.pocetak = novicvor
            self.kraj = novicvor
            print("Lista je bila prazna. Početak i kraj liste su sada isti novi čvor!")
        else:                               
            self.kraj.sljedeci = novicvor      
            self.kraj = novicvor                
            print("Uspješno dodan element na kraj liste!")
        
        self.dduzina += 1

    def umetni(self, x):
        privremin = Cvor(x)

        if (self.lduzina == 0):
            privremin.sljedeci = self.pocetak
            self.pocetak = privremin
            if(self.lduzina+self.dduzina == 0):
                self.kraj = privremin
            print("Uspješno umetnut element " + str(x) + " na početak liste")
        else:
            privremin.sljedeci = self.tekuci.sljedeci
            self.tekuci.sljedeci = privremin
            if(self.dduzina == 0):
                self.kraj = self.tekuci.sljedeci
            print("Uspješno umetnut element " + str(x) + " na poziciju pokazivača " + str(self.tekuci))
        
        self.dduzina += 1    

    def izbaci(self):
        if (self.dduzina <= 0):
            print("Nema elemenata za izbacivanje/brisanje! Tekući na kraju liste!")
        
        privremen = Cvor()
        
        if(self.lduzina == 0):                      
            privremin = self.pocetak
            self.pocetak = privremin.sljedeci
            print("Izvršeno je izbacivanje elementa!")
        else:
           privremen = self.tekuci.sljedeci        
           self.tekuci.sljedeci = privremen.sljedeci
           print("izvršeno je izbacivanje elementa!")
        
        if(self.dduzina == 1):                  
            self.kraj = self.tekuci
        
        self.dduzina -= 1

    def ispisiTekuci(self):
        if (self.dduzina == 0):
            print("Nema elemnata za ispis! Pokazivač je na kraju liste!")
        elif(self.tekuci == None):
            print("Vrijednost elementa na početku liste je: " + str(self.pocetak.element))
        else:
            print("Vrijednost elementa na tekućoj poziciji je: " + str(self.tekuci.element))

    def prikazi(self):
        if(self.dduzina + self.lduzina == 0):
            print("Lista je prazna!")
        else:
            privremeni = self.pocetak
            brojac = 0

            while(privremeni != None):
                print(str(brojac) + ": " + str(privremeni), end="")

                if (privremeni == self.pocetak):
                    print( " <- početak",end="")
                if(privremeni == self.tekuci):
                    print( " <- tekući",end="")
                if(privremeni == self.kraj):
                    print( " <- kraj",end="")
                print("")

                privremeni = privremeni.sljedeci
                brojac += 1