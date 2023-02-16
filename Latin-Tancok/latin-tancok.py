print("1.Feladat")
"""
Egy nagy listában fogom tárolni az adatokat aminek az egyes táncra vonatkozó elemei szótárak lesznek.
"""
adatok = []
tancok = []
tanc = {}

with open("tancrend.txt", "r", encoding="utf-8") as file:
    for sor in file:
        if len(sor) == 3:
            adatok.append(sor.strip())
            tanc["nev"] = adatok[0]
            tanc["lany"] = adatok[1]
            tanc["fiu"] = adatok[2]
            tancok.append(tanc)
            adatok = []
            szotar = {}
print(tancok)