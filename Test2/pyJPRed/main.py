import pyJPRed
import zadatak1

# Ispis menija
print("      ** TESTNI PROGRAM ZA pyRed **")
print("-------------------Menu--------------------")
print("1. Dodaje element u red")
print("2. Ukloni element iz reda")
print("3. Element na početku reda")
print("4. Prikazi sadrzaj reda")
print("5. Da li je red prazan?")
print("6. Da li je red pun?")
print("7. Potpuno brisanje reda!")
print("8. Aritmeticka sredina elemenata reda")
print("9. Minimalni element reda")
print("10. Testna funkcija")
print("99. Izlaz")

unos_izbor = input("--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

# Iniciranje JP Reda
Red = zadatak1.prosireniPyJPRed()

# case petlja za definiranje opcija u meniju
def menu(izbor):
    match izbor:
        case 1:
            x = input("Unesite vrijednost elementa za dodavanje u red?\n")
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
            print("Kapacitet JPReda je \"neograničen!\"")
        case 7:
            Red.brisi()
        case 8:
            Red.ariSredina()
        case 9:
            Red.dajMinimum()
        case 10:
            testni = [8,6,9,2,3,1,5,5,9,7]
            for i in range(len(testni)):
                Red.dodajURed(testni[i])
            Red.prikazi()
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