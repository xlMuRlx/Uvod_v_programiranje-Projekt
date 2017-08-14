import kviz
import tkinter as tk
import random
from random import randint


stevec = 0
vpr = None
polovicke = 0



def naslednje_vprasanje():
    global vpr
    global stevec
    if stevec == 0:
        vprasanje.config(text=kviz.uvod)
        odgovorA.config(text="Začni kviz", command=zacni_igro)
        odgovorB.config(text="Pravila", command=ukaz_pravila, state="normal")
        odgovorC.config(text="Zapri", command=zakljucek, state="normal")
        odgovorD.config(text="", state="disabled")
        
    if stevec <= 4 and stevec > 0:
        i = randint(0,len(lahkavprasanja)-1)
        vpr = lahkavprasanja.pop(i)
        
    if stevec > 4 and stevec <= 8:
        i = randint(0,len(tezkavprasanja)-1) 
        vpr = tezkavprasanja.pop(i)
        
    if stevec > 8 and stevec <= 12:
        i = randint(0,len(tezjavprasanja)-1) 
        vpr = tezjavprasanja.pop(i)
        
    if stevec > 12 and stevec <= 16:
        i = randint(0,len(najtezjavprasanja)-1) 
        vpr = najtezjavprasanja.pop(i)
        
    if stevec == 1:
        polovicka.config(text="50/50", state="normal")
        osvojen_znesek.config(text="Osvojeno: 0€")
        
    if stevec != 0: 
        vprasanje.config(text=str(stevec) + ". " + vpr.vprasanje)
        odgovorA.config(text=vpr.odgovori[0], command=izberi_odgovor_A, state="normal")
        odgovorB.config(text=vpr.odgovori[1], command=izberi_odgovor_B, state="normal")
        odgovorC.config(text=vpr.odgovori[2], command=izberi_odgovor_C, state="normal")
        odgovorD.config(text=vpr.odgovori[3], command=izberi_odgovor_D, state="normal")
        stevec += 1
        



def izberi_odgovor(odg):
    global vpr
    pravilno = vpr.izberi_odgovor(odg)

    if pravilno:
        if stevec == 17:
            vprasanje.config(text="Čestitamo, postali ste milijonar! Osvojili ste " + \
                         kviz.denarne_nagrade[stevec-1] + "!")
            odgovorA.config(text="Zaključi", command=zakljucek, state="normal")
            odgovorB.config(text="Nazaj", command=nazaj, state="normal")
            odgovorC.config(text="", state="disabled")
            odgovorD.config(text="", state="disabled")
            polovicka.config(state="disabled")
            osvojen_znesek.config(text="")
        else:
            osvojen_znesek.config(text="Osvojeno: {0}".format(kviz.denarne_nagrade[stevec-1]))
            naslednje_vprasanje()

    else:
        vprasanje.config(text="Konec igre, osvojili ste " + \
                         kviz.denarne_nagrade[stevec-2])
        odgovorA.config(text="Zaključi", command=zakljucek, state="normal")
        odgovorB.config(text="Nazaj", command=nazaj, state="normal")
        odgovorC.config(text="", state="disabled")
        odgovorD.config(text="", state="disabled")
        polovicka.config(text= "", state="disabled")
        osvojen_znesek.config(text="")

    
def izberi_odgovor_A():
    izberi_odgovor(0)
def izberi_odgovor_B():
    izberi_odgovor(1)
def izberi_odgovor_C():
    izberi_odgovor(2)
def izberi_odgovor_D():
    izberi_odgovor(3)


def zacni_igro():
    global lahkavprasanja
    global tezkavprasanja
    global tezjavprasanja
    global najtezjavprasanja
    	
    lahkavprasanja = kviz.poisci_vprasanja("Lahka_vprasanja.txt")
    tezkavprasanja = kviz.poisci_vprasanja("Tezka_vprasanja.txt")
    tezjavprasanja = kviz.poisci_vprasanja("Tezja_vprasanja.txt")
    najtezjavprasanja = kviz.poisci_vprasanja("Najtezja_vprasanja.txt")

    global stevec
    stevec = 1
    naslednje_vprasanje()


def zakljucek():
    okno.destroy()


def ukaz_pravila():
    vprasanje.config(text=kviz.pravila_igre)
    odgovorA.config(text="Nazaj", command=nazaj)
    odgovorB.config(text="", state="disabled")
    odgovorC.config(text="", state="disabled")
    odgovorD.config(text="", state="disabled")


def nazaj():
    global stevec
    stevec = 0
    naslednje_vprasanje()


def polovica():
    global vpr
    global polovicke
    seznam = []
    gumbi = ["A", "B", "C", "D"]
    pravilni = vpr.pravilni_odgovor
    for i in range(4):
        if i != pravilni:
            seznam.append(i)

    random.shuffle(seznam)

    prvi = gumbi[seznam[0]]
    drugi = gumbi[seznam[1]]

    if prvi == "A" or drugi == "A":
        odgovorA.config(state="disabled")
    if prvi == "B" or drugi == "B":
        odgovorB.config(state="disabled")
    if prvi == "C" or drugi == "C":
        odgovorC.config(state="disabled")    
    if prvi == "D" or drugi == "D":
        odgovorD.config(state="disabled")

    if polovicke == 1:
        polovicka.config(state="disabled")

    polovicke = 1

  

okno = tk.Tk()


vprasanje = tk.Label(okno, text="")
odgovorA = tk.Button(okno, text="", height=1, width=50, \
                     command=izberi_odgovor_A)
odgovorB = tk.Button(okno, text="", height=1, width=50, \
                     command=izberi_odgovor_B)
odgovorC = tk.Button(okno, text="", height=1, width=50, \
                     command=izberi_odgovor_C)
odgovorD = tk.Button(okno, text="", height=1, width=50, \
                     command=izberi_odgovor_D)

polovicka = tk.Button(okno, text="", height=1, width=20, \
                       command=polovica, state="disabled")
osvojen_znesek = tk.Label(okno, text="", height=1, width=20)


odgovorA.grid(row=2, column=1)
odgovorB.grid(row=2, column=2)
odgovorC.grid(row=3, column=1)
odgovorD.grid(row=3, column=2)

polovicka.grid(row=2, column=3)
osvojen_znesek.grid(row=3, column=3)


vprasanje.grid(row=1, column=1, columnspan=2)

naslednje_vprasanje()
okno.mainloop()

