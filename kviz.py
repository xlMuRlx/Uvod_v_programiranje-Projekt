import random


class Vprasanje:

    def __init__(self, vprasanje):
        self.vprasanje = vprasanje
        self.odgovori = []
        self.pravilni_odgovor = []

    def __repr__(self):
        return "Vprasanje({0}, {1},{2})".format(self.vprasanje, self.odgovori, \
                                                self.pravilni_odgovor)



def poisci_vprasanja(datoteka):
    vprasanja = []
    with open (datoteka) as datoteka:
        for vrstica in datoteka:
            zacetni_element = vrstica[0]
            if zacetni_element == "+":
                dolzina = len(vrstica)
                vprasanje = vrstica[2:dolzina - 1]
                nov_element = Vprasanje(vprasanje)
            elif zacetni_element in "ABCD":
                if "*" in vrstica:
                    odgovor = vrstica.replace("*", "")
                    odgovor2 = odgovor.replace("\n", "")
                    nov_element.pravilni_odgovor.append(odgovor2.strip())
                    nov_element.odgovori.append(odgovor2)
                else:
                    odgovor = vrstica.replace("\n", "")
                    nov_element.odgovori.append(odgovor)
            elif vrstica == "\n":
                vprasanja.append(nov_element)
                
    return vprasanja


def postavi_vprasanje(datoteka):
    vprasanja = poisci_vprasanja(datoteka)
    vprasanje = random.choice(vprasanja)
    return vprasanje



postavi_vprasanje("Lahka_vprasanja.txt")     

