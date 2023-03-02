"""
Készítsen egy programot, amely rögzíti és elemzi a felhasználó által megadott szavak
listáját! A program forráskódját mentse “szolista” néven!
"""
print('1.Feladat')
"""
1. A mintának megfelelően a felhasználótól kérjen be legalább 4 betűs szavakat
vesszővel és szóközzel elválasztva!
"""
tarolt_szavak = []
szavak = input("Adj meg legalább 4 betűs szavakat vesszővel és szóközzel elválasztva! ")

print("\n2.Feladat")
"""
Állapítsa meg hogy a megadott szavak között van-e olyan, amely többször is
előfordul.
"""
ismetlodes = 0
tarolt_szavak2 = []
for i in szavak.split():
    tarolt_szavak.append(i)
    if i not in tarolt_szavak2:
        tarolt_szavak2.append(i)
    else:
        ismetlodes += 1
if ismetlodes > 0:
    print("Van ismétlődés")

print("\n3.Feladat")
"""
3. A képernyőn jelenítse meg a legrövidebb szót ill. szavakat!
"""
legrovidebb_szavak = "kkkkkkkkkkkkkkkkkkkkkkkkkkk"

for szo in tarolt_szavak2:
    if len(legrovidebb_szavak) > len(szo):
        legrovidebb_szavak = szo
print("A legrövidebb szó:", legrovidebb_szavak)

print("\n4.Feladat")
"""
4. Írja ki a leghosszabb szót - amennyiben több ilyen is létezik, akkor az egyik
leghosszabb szót - úgy, hogy az első és utolsó betűje a helyén marad, a szó
belsejében lévő betűk azonban fordított sorrendben szerepelnek! Például zsiráf >
zárisfs
"""


