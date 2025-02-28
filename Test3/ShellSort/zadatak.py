import pyPretrazivanja
import pyNizListe

class prosirenapyPretrazivanja(pyPretrazivanja.pyPretrazivanjeNizListe):

    def __init__(self, kapacitet):
        super().__init__(kapacitet)

    def shellSortM(self):
        # Ručno definirana lista razmaka
        razmaci = [99, 11, 1]

        print("Lista razmaka:", razmaci)

        # Ispis početne liste
        pocetna_lista = [self.Niz[i] for i in range(self.duzina)]
        print("Početna lista:", pocetna_lista)

        for razmak in razmaci:
            for i in range(razmak, self.duzina):
                privremeni = self.Niz[i]
                j = i
                while j >= razmak and self.Niz[j - razmak] > privremeni:
                    self.Niz[j] = self.Niz[j - razmak]
                    j -= razmak
                self.Niz[j] = privremeni

        # Ispis završne liste
        zavrsna_lista = [self.Niz[i] for i in range(self.duzina)]
        print("Završna lista:", zavrsna_lista)

    def minElement(self):
        if self.duzina == 0:
            print("Lista je prazna!")
            return None
        minimum = self.Niz[0]
        for i in range(1, self.duzina):
            if self.Niz[i] < minimum:
                minimum = self.Niz[i]
        print("Minimalni element u listi je:", minimum)
        return minimum
