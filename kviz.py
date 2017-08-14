

import random


class Vprasanje:

    def __init__(self, vprasanje):
        self.vprasanje = vprasanje
        self.odgovori = []
        self.pravilni_odgovor = -1

    def __repr__(self):
        return "Vprasanje({0}, {1},{2})".format(self.vprasanje, self.odgovori, \
                                                self.pravilni_odgovor)

    def izberi_odgovor(self, odg):
        return odg == self.pravilni_odgovor
    


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
    random.shuffle(vprasanja)
    
    return random.choice(vprasanja)


denarne_nagrade = ["0€", "50€", "100€", "200€", "300€", "500€", "750€", \
                   "1500€", "2500€", "3500€", "5000€", "7500€", "12500€", \
                   "20000€", "30000€", "50000€", "100000€"]

uvod = "Dobrodošli v kvizu Lepo je biti milijonar."

pravila_igre = '''
    Pravila kviza:
    
    Pravila so enostavna. Potrebno je odgovoriti na 16 vprašanj. Vsako vprašanje ima štiri
    ponujene odgovore, med katerimi je samo eden pravilen. Vsako vprašanje je vredno določen
    znesek denarja, ki ga tekmovalec osvoji, če nanj pravilno odgovori. Prva štiri vprašanja
    so načeloma lahka, nato se težavnost vprašanj stopnjuje k vedno bolj težkim. Če tekmovalec
    napačno odgovori na vprašanje osvoji znesek pri prejšnem vprašanju. Igra se zaključi, ko
    tekmovalec narobe odgovori na neko vprašanje ali pa pravilno odgovori na vseh 16 vprašanj.

    Tekmovalec ima dvakrat na voljo tudi pomoč 50/50, pri kateri odpadeta dva naključno izbrana
    nepravilna odgovora.
    '''

