# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 22:39:24 2021

@author: Emil
"""

class spill():
    def __init__(self, spm, fv, svar):
        self.spørsmål = spm
        self.flervalg = fv
        self.svar = svar
        
    def __str__(self):
        return self.spørsmål + "\n" + "\n".join([" ".join([str(x+1), y]) for x, y in enumerate(self.flervalg)]) + "\n"
    
    def sjekk_svar(self, brukerSvar):
        return brukerSvar == self.svar

    def korrekt_svar_tekst(self):
        return self.flervalg[self.svar]


def les():
    with open("sporsmaalsfil.txt", encoding = "UTF-8") as fil:
        liste = []
        for i, e in enumerate(fil):
            e = e.split(":")
            globals()["spørsmål%s" % i] = spill(e[0], e[2].strip("[]\n ").split(", "), int(e[1]))
            liste.append(eval("spørsmål%s" % i))
        return liste

   

class Spiller():
    def __init__(self, navn):
        self.navn = navn
        self.poengsum = 0
        self.forrigepoengsum = 0


listeMedSpillere = []
def lagSpillere():
    for i in range(1,int(input("Hvor mange spillere er det?: "))+ 1):
        globals()["spiller%s" % i] = Spiller(input("Hva er navnet ditt?: "))
        
        exec("listeMedSpillere.append(spiller" + str(i) + ")")
        

if __name__ == "__main__":
    lagSpillere()
    liste = les()
    
    for i in liste:
        print(i.__str__())
        for s in listeMedSpillere:

            svar = int(input(f"Velg svaralternativ for {s.navn}: "))
            

            if svar==i.svar+1: s.poengsum += 1
        print("Korrekt svar: " , i.korrekt_svar_tekst() )
        for s in listeMedSpillere:

            print (f"{s.navn}: ", "Korrekt" if s.forrigepoengsum + 1 == s.poengsum else "Feil")
            s.forrigepoengsum = s.poengsum
    
    for s in listeMedSpillere:

        print (f"{s.navn} fikk {s.poengsum} riktige svar!")























































"""    
spørsmål1 = spill("Gvem spiller gitar i Guns'N'Roses?",["Nils Oktober", "Phoenix Wright", "Slash", "Steve McQueen"],3)
spørsmål2 = spill("Hvilken farge er en vanlig pringles boks?",["Rød", "Gul", "Grønn", "Blå"],1)

print(spørsmål1.__str__())
score = 0
goomba =spørsmål1.sjekk_svar(int(input("hva tror du svaret er? ")))
if goomba == True:
    print("Nice Riktig svar", "\n")
    score=+1
elif goomba == False:
    print("Uffda det var feil", "\n")

print(spørsmål2.__str__())

goomba1 =spørsmål2.sjekk_svar(int(input("hva tror du svaret er? ")))
if goomba1 == True:
    print("Nice, det var også riktig", "\n")
    score=+1
elif goomba1 == False:
    print("Uffda det var feil", "\n")
    
print("din totale poengsum ble:",score,"ut av 2")
"""


        

