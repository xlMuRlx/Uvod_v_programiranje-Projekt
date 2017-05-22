

import random


class Vprasanje:

    def __init__(self, vprasanje):
        self.vprasanje = vprasanje
        self.odgovori = []
        self.pravilni_odgovor = -1

    def __repr__(self):
        return "Vprasanje({0}, {1},{2})".format(self.vprasanje, self.odgovori, \
                                                self.pravilni_odgovor)

    def izberi_odgovor_A(self):
        return self.odgovori[0]

    def izberi_odgovor_B(self):
        return self.odgovori[1]

    def izberi_odgovor_C(self):
        return self.odgovori[2]

    def izberi_odgovor_D(self):
        return self.odgovori[3]


def poisci_vprasanja(datoteka):
    '''Funkcija iz datoteke razbere vprašanja ter
    pripadajoče odgovore s pravilnim vred.'''
    vprasanja = []
    with open (datoteka) as file:
        for vrstica in file:
            zacetni_element = vrstica[0]
            if zacetni_element == "+":
                dolzina = len(vrstica)
                vprasanje = vrstica[2:dolzina - 1]
                nov_element = Vprasanje(vprasanje)
            elif zacetni_element in "ABCD":
                if "*" in vrstica:
                    odgovor = vrstica.replace("*", "")
                    odgovor2 = odgovor.replace("\n", "")
                    nov_element.pravilni_odgovor = ord(zacetni_element) - ord("A")
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
    stevec = 0
    while True:
        if vprasanje == 1:
            vprasanja = poisci_vprasanja("Lahka_vprasanja.txt")
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break
        
        elif vprasanje < 4:
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break
            
        elif vprasanje == 4:
            vprasanja = poisci_vprasanja("Tezka_vprasanja.txt")
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break
            
        elif vprasanje < 7:
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break

        elif vprasanje == 7:
            vprasanja = poisci_vprasanja("Tezja_vprasanja.txt")
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break

        elif vprasanje < 10:
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break

        elif vprasanje == 10:
            vprasanja = poisci_vprasanja("Najtezja_vprasanja.txt")
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break

        elif vprasanje < 12:
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Bravo, osvojili ste {0}!".format(denarne_nagrade[stevec]))
                vprasanje += 1
                stevec += 1
            else:
                print("KONEC!")
                break

        elif vprasanje == 12:
            random.shuffle(vprasanja)
            odgovori_na = vprasanja.pop()
            print(vprasanje, ".", odgovori_na.vprasanje)
            print(odgovori_na.odgovori)
            moj_odgovor = int(input("Odgovor: "))
            if moj_odgovor == odgovori_na.pravilni_odgovor:
                print("Postali ste milijonar!")
                break
            else:
                print("KONEC!")
                break
