"""
Készítsen egy programot, amely rögzíti és elemzi a felhasználó által megadott szavak
listáját! A program forráskódját mentse “szolista” néven!
"""
import random

"""
1. A mintának megfelelően a felhasználótól kérjen be legalább 4 betűs szavakat
vesszővel és szóközzel elválasztva!
"""
szavak = ["alma", "lapát", "hűtőszekrény", "alma", "tető"]#input("Adj meg legalább 4 betűs szavakat vesszővel és szóközzel elválasztva! ")

print("\n2.Feladat")
"""
Állapítsa meg hogy a megadott szavak között van-e olyan, amely többször is
előfordul.
"""
for index in szavak:
    if szavak.count(index) > 1:
        print("A szavak listájában van ismétlődés.")
        break

print("\n3.Feladat")
"""
3. A képernyőn jelenítse meg a legrövidebb szót ill. szavakat!
"""
minimumkereso = min(szavak)
legrovidebb_szavak = []

print("A legrövidebb szó/szavak a szólistában:")
for szo in szavak:
    if len(szo) == len(minimumkereso) and szo not in legrovidebb_szavak:
        legrovidebb_szavak.append(szo)

print(f"A legrövidebb szó/szavak a szólistában: {legrovidebb_szavak}")

print("\n4.Feladat")
"""
4. Írja ki a leghosszabb szót - amennyiben több ilyen is létezik, akkor az egyik
leghosszabb szót - úgy, hogy az első és utolsó betűje a helyén marad, a szó
belsejében lévő betűk azonban fordított sorrendben szerepelnek! Például zsiráf >
zárisfs
"""
maxkereso = ""

for szo in szavak:
    if len(szo) > len(maxkereso):
        maxkereso = szo

print(maxkereso)
belso = maxkereso[1:11]
print(belso)
indexek = ""
for index in belso:
    kevert_betu = random.choice(belso)
    if kevert_betu not in indexek:
        indexek += kevert_betu
print(indexek)