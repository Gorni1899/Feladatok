print("1.Feladat")
"""
Egy nagy listában fogom tárolni az adatokat aminek az egyes táncra vonatkozó elemei szótárak lesznek.
"""
adatok = []
tancok = []
tanc = {}

with open("tancrend.txt", "r", encoding="utf-8") as file:
    for sor in file:
        adatok.append(sor.strip())
        if len(adatok) == 3:
            tanc["nev"] = adatok[0]
            tanc["lany"] = adatok[1]
            tanc["fiu"] = adatok[2]
            tancok.append(tanc)
            adatok = []
            szotar = {}

# teszt kiíratás
print(tancok)

print("\n2.Feladat")
"""
Két print utasítást fogok használni és f sztringet
"""
#2. Írassa ki a képernyőre, hogy melyik volt az elsőként és melyik az utolsóként bemutatott tánc neve!
print(f"Az elsőként bemutatott tánc neve a {tancok[0]['nev']} volt.")
print(f"Az utolsóként bemutatott tánc neve a {tancok[-1]['nev']} volt.")