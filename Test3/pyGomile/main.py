import pyGomile, zadatak
from zadatak import prosirenaPyGomila

# Ispis menija
print("      ** TESTNI PROGRAM ZA pyGomile **")
print("-------------------Menu--------------------")
print("1. Učitavanje niza")
print("2. Stvaranje gomile iz neuređenog niza")
print("3. Ispis sadržaja gomile")
print("4. Umetanje novog elementa u gomilu")
print("5. Izbacivanje prvog elementa iz gomile")
print("6. Izbacivanje elementa iz gomile sa proizvoljne pozicije")
print("7. Promjena vrijednosti elementa")
print("8. Kub sume elemenata")
print("9. Dodaj testne elemente")
print("99. Izlaz")

def testnaFunkcija():
    test = [1,45,67,8,9,-43,2,87]
    print(f"Unos testnih elemenata u gomilu: {test}")
    for x in test:
        Gomila.umetniUGomilu(x)
    Gomila.prikazi(Gomila.velicina)

# Iniciranje Gomila, tipa max i min
print("\n-------------Odaberite TIP gomile--------------")
izbortipa = input("Unesite vrijednost 'max' ili 'min' za odabir tipa Gomile!\n")

maxduzina = 20

if (izbortipa == "max"):
    Gomila = zadatak.prosirenaPyGomila(maxduzina,pyGomile.maxTip())
elif(izbortipa == "min"):
    Gomila = zadatak.prosirenaPyGomila(maxduzina,pyGomile.minTip())
else:
    print("Progrešan odabir!\nProgram završen!")
    exit()

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# case petlja za definiranje opcija u meniju
def menu(izbor):
    match izbor:
        case 1:   
            n = input("Unesite broj elemenata niza koji je maksimalno 20!\n")
            n = int(n)
            if(n<=20):
                Gomila.ucitaj(n)
            elif((n>20) or (n<1)):
                print("Broj elemenata preko maksimalnog kapaciteta od 20 ili manji od jedan!")            
        case 2:
            Gomila.stvoriGomilu()
        case 3:            
            Gomila.prikazi(Gomila.velicina)
        case 4:
             x = input("Unesite vrijednost novog elementa za dodavanje u gomilu?\n")            
             Gomila.umetniUGomilu(int(x))
        case 5:  
            Gomila.izbaciPrvi()
        case 6:
            i = input("Unesite poziciju elementa za brisanje?\n")            
            Gomila.izbac(int(i))   
        case 7:
            i = input("Unesite poziciju elementa za izmjenu vrijednosti?\n")
            x = input("Unesite novu vrijednost elementa?\n")            
            Gomila.promjeniKljuc(int(i),int(x))
        case 8:
            Gomila.KubSume()
        case 9:
            testnaFunkcija()
        case 10:
            Gomila.dajMin()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

# while petlja za kontinuiran odabir opcija u meniju
while (izbor):
    menu(izbor)
    unos_izbor = input("--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)

# UNZE PTF ASP 2021/2022 :: M.S. :: 12.01.2022