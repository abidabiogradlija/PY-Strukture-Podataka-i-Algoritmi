import pyHash
import zadatak
print("-------------------Menu--------------------")
print("------ LINEARNO HEŠIRANJE ------")
print("1. Umetanje elemenata u tabele")
print("2. Pretraživanje tabele")
print("3. Prikaz sadržaja tabele")
print("------ DVOSTRUKO HEŠIRANJE ------")
print("4. Umetanje elemenata u tabelu")
print("5. Pretraživanje tabele")
print("6. Prikaz sadržaja tabele")
print("7. TEST")

print("99. Program završen")

def testnaFunkcija():
    test=[-3,19,8,5,-3,19,2,-3,19,7]
    for x in test:
        T1.umetniHash(x)
    T1.izbaciElemente()

praznoMjesto = None    
velicinaLinearno = 10   
velicinaDvostruko = 13  

T1 = zadatak.prosirenipyHash(velicinaLinearno, praznoMjesto)
T2 = pyHash.DvostrukiHash(velicinaDvostruko, praznoMjesto)  

unos_izbor = input("\n--------------Izaberite opciju?---------------\n")
izbor = int(unos_izbor)

def menu(izbor):
    match izbor:
        case 0:
            return 0
        case 1:
            x = int(input("Upisite cjelobrojnu vrijednost za unos u tabelu linearnog heširanja:\n"))
            if T1.umetniHash(x):
                print("Element je pohranjen u tabelu linearnog heširanja.\n")
            else:
                print("Element nije pohranjen u tabeli linearnog heširanja. Kapacitet tabele je u potpunosti popunjen!\n")
        case 2:
            x = int(input("Unesite broj kojeg pretražujemo u tabeli linearnog heširanja:\n"))
            p = T1.traziHash(x)
            if p != None:
                print("Element " + str(x) + " je pronađen, na indeksu " + str(p))
            else:
                print("Element nije pronađen")
        case 3:
            print("Sadržaj tabele linearnog heširanja:\n")
            T1.prikazi()
        case 4:
            x = int(input("Unesite cjelobrojnu vrijednost za unos u tabelu dvostrukog heširanja:\n"))
            if T2.umetniHash(x):
                print("Element je pohranjen u tabelu dvostrukog heširanja.\n")
            else:
                print("Element nije pohranjen u tabeli dvostrukog heširanja. Kapacitet tabele je u potpunosti popunjen!\n")
        case 5:
            x = int(input("Unesite broj kojeg pretražujemo u tabeli dvostrukog heširanja:\n"))
            p = T2.traziHash(x)
            if p != None:
                print("Element " + str(x) + " je pronađen, na indeksu " + str(p))
            else:
                print("Element nije pronađen")
        case 6:
            print("Sadržaj tabele dvostrukog heširanja:\n")
            T2.prikazi()
        case 7:
            testnaFunkcija()
        case 99:
            print("Program završen!")
            exit()
      
        case _:
            print("Pogrešan izbor. Molimo ponovite unos izbora!")

while (izbor):
    menu(izbor)
    unos_izbor = input("\n--------------Izaberite opciju?---------------\n")
    izbor = int(unos_izbor)


# UNZE PTF ASP 2021/2022 :: M.S. :: 19.01.2022