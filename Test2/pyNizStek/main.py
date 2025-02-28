import pyNizStek
import zadatak
# Ispis menija
print("      ** TESTNI PROGRAM ZA pyStek **")
print("-------------------Menu--------------------")
print("1. Dodaje element na stek")
print("2. Ukloni element sa steka")
print("3. Element na vrhu steka")
print("4. Prikazi sadrzaj steka")
print("5. Da li je stek prazan?")
print("6. Da li je stek pun?")
print("7. Potpuno brisanje steka!")
print("8. TEST")

print("99. Izlaz")

def testnaFunkcija():
    test=[2,9,8,5,11,9,5,7,6,3]
    for x in test:
        Stek.dodajNaStek(x)
    print("ELEMENTI SU:")
    Stek.prikazi()
    Stek.dodajMini()
unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje Niz Steka
k = 11
Stek = zadatak.prosireniStek(k)

# case petlja za definiranje opcija u meniju
def menu(izbor):
    match izbor:
        case 1:
            x = input("Unesite vrijednost elementa za dodavanje na stek?\n")
            Stek.dodajNaStek(x)
        case 2:
            Stek.ukloniSaSteka()
        case 3:
            Stek.elementNaVrhu()
        case 4:
            Stek.prikazi()
        case 5:  
            print("Vrh: " + str(Stek.vrh))
            print("Kapacitet: " + str(Stek.kapacitet))          
            if(Stek.jeLiPrazan()):
                print("Stek je prazan!")
            else:
                print("Stek NIJE prazan!")
        case 6:
            print("Vrh: " + str(Stek.vrh))
            print("Kapacitet: " + str(Stek.kapacitet))  
            if(Stek.jeLiPun()):
                print("Stek je pun!")
            else:
                print("Stek NIJE pun!")   
        case 7:
            Stek.brisi()
        case 8:
            testnaFunkcija()
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

# UNZE PTF ASP 2021/2022 :: M.S. :: 01.12.2021