import pyCRed
import zadatak
# Ispis menija
print("      ** TESTNI PROGRAM ZA pyRed **")
print("-------------------Menu--------------------")
print("1. Dodaje element u red")
print("2. Ukloni element iz reda")
print("3. Element na početku reda")
print("4. Prikazi sadržaj reda")
print("5. Da li je red prazan?")
print("6. Da li je red pun?")
print("7. Potpuno brisanje reda!")
print("8. TEST!")

print("99. Izlaz")
def testnaFunkcija():
    test=[3,5,8,5,6,9,2,1,9,7]
    for x in test:
        Red.dodajURed(x)
    print("NOVA LISTA ELEMENATA:")
    Red.prikazi()
    Red.prebrojManje()
unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje Cirkularnog Reda
k = 10
Red = zadatak.prosirenipyCRed(k)

# case petlja za definiranje opcija u meniju
def menu(izbor):
    match izbor:
        case 1:
            x = input("Unesite vrijednost elementa za dodavanje na red?\n")
            Red.dodajURed(x)
        case 2:
            Red.izbaciIzReda()
        case 3:
            Red.elementNaCelu()
        case 4:
            Red.prikazi()
        case 5:        
            if(Red.jeLiPrazan()):
                print("Red je prazan!")
            else:
                print("Red NIJE prazan!")
        case 6:
            if(Red.jeLiPun()):
                print("Red je pun!")
            else:
                print("Red NIJE pun!")   
        case 7:
            Red.brisi()
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