"""
Készítsen egy programot, amely rögzíti és elemzi a felhasználó által megadott szavak
listáját! A program forráskódját mentse “szolista” néven!
"""
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
maxkereso = ""

for index in szavak:
    if len(index) > len(maxkereso):
        maxkereso = index

minkereso = ""
print("A legrövidebb szavak:")
legrovidebb_szavak = []
for index in szavak:
    if len(index) < len(maxkereso):
        minkereso = index
        legrovidebb_szavak.append(minkereso)
print(minkereso)


