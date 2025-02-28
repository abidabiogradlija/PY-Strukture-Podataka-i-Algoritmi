import pyBSP
import zadatak


print("      ** TESTNI PROGRAM ZA pyBSP - Binarno Stablo Pretraživanja **")
print("-------------------Menu--------------------")
print("1. Umetni broj u stablo - REKURZIVNO")
print("2. Umetni broj u stablo - ITERATIVNO")
print("3. Brisanje čvora")
print("4. Preorder obilazak stabla")
print("5. Inorder obilazak stabla")
print("6. Postorder obilazak stabla")
print("7. Visina stabla")
# --
print("8. Rekurzivno pretrazivanje stabla")
print("9. Iterativno pretrazivanje stabla")
print("10. Minimalan element u stablu")
print("11. Maksimalan element u stablu")
print("12. Testna funkcija")
print("13. Aritmeticka sredina")



# --
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)


Stablo = zadatak.prosirenipyBSP()

def testnaFunkcija():
    test=[8,6,9,2,3,1,5,5,9,7]
    for x in test:
        Stablo.umetniIterativno(x)
def menu(izbor):
    match izbor:
        case 1:
            x = input("Unesite vrijednost elementa!\n")
            Stablo.umetniRekurzivno(Stablo.korijen, int(x))
        case 2:
            x = input("Unesite vrijednost elementa!\n")
            Stablo.umetniIterativno(int(x))
        case 3:
            x = input("Unesite vrijednost elementa za brisanje!\n")
            if(Stablo.brisiCvor(Stablo.korijen, int(x))):
                print("Čvor izbrisan!")
            else:
                print("Čvor nije izbrisan!")
        case 4:
            Stablo.preorder(Stablo.korijen)
        case 5:            
            Stablo.inorder(Stablo.korijen)
        case 6:
            Stablo.postorder(Stablo.korijen)
        case 7:
            Stablo.visina(Stablo.korijen)
        case 8:
            kljuc = input("Unesite ključnu vrijednost za pretragu!\n")
            if(Stablo.traziRekurzivno(Stablo.korijen,int(kljuc)) != None):
                print("\nElement pronađen!\n")
            else:
                print("\nElement nije pronađen!\n")
        case 9:
            kljuc = input("Unesite ključnu vrijednost za pretragu!\n")
            if(Stablo.traziIterativno(Stablo.korijen,int(kljuc)) != None):
                print("\nElement pronađen!\n")
            else:
                print("\nElement nije pronađen!\n")
        case 10:
            Stablo.minimalniElement()
        case 11:
            print("Maksimalna vrijednost u stablu je: " + str(Stablo.maxCvor(Stablo.korijen).element))
        case 12:
            testnaFunkcija()
        case 13:
            Stablo.aritmetickaSr()
        case 99:
            print("Program završen!\n")
            exit()
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")


while (izbor):
    menu(izbor)
    unos_izbor = input("\n--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)

