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
    '''Funkcija iz datoteke razbere vprašanja ter
    pripadajoče odgovore s pravilnim vred.'''
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
    '''Iz podane datoteka funkcija izbere le eno naključno vprašanje.'''
    vprasanja = poisci_vprasanja(datoteka)
    vprasanje = random.choice(vprasanja)
    return vprasanje

denarne_nagrade = ["100€", "200€", "500€", "750€", \
                   "1500€", "2500€", "5000€", "7500€", "12500€", \
                   "25000€", "50000€", "100000€"]

#Igra bo imela v vsakem sklopu po 3 vprašanja

def igra():
    vprasanje = 1
    if vprasanje == 1:
        with open("Lahka_vprasanja.txt") as datoteka:
            vprasanja = poisci_vprasanja(datoteka)
            random.shuffle(vprasanja)
            odgovori_na = vprasanje.pop()
            moj_odgovor = input("Odgovor: ")
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                vprasanje += 1
                igra()
#izberi odgovor
#če je odgovor napačen --> konec
#če je odgovor pravilen --> vprasanje += 1 in izpiše nagrado
        
    elif vprasanje < 4:
        random.shuffle(vprasanja)
        odgovori_na = vprasanje.pop()
        return odgovori_na
#enak postopek za težja vprašanja

