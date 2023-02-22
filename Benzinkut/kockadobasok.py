import random
"""
Botondnak egy társasjátékban minden körben egy hatlapú dobókockával kellett dobnia.
A dobásnak megfelelő számú mezőt léphetett a táblán előre.
A program forráskódját mentse “kockadobasok” néven!

"""
print("1.Feladat")
# 1. Olvassa be a mintának megfelelően, és tárolja el, hogy hány dobás volt a játékban!
dobasok_szama = int(input("Add meg a dobások számát: "))

print("\n2.Feladat")
"""
2. Botond dobásait most a program által generált véletlenszámok helyettesítsék,
melyek kerüljenek tárolásra is! Tetszőleges formátumban jelenítse meg a képernyőn
a dobásokat.
"""
tarolt_dobasok = []
for dobas in range(dobasok_szama):
    veletlenszamok = random.randint(1,6)
    tarolt_dobasok.append(veletlenszamok)

print("A dobások: ",tarolt_dobasok)

print("\n3.Feladat")
"""
3. A mintának megfelelően adja meg, hogy Botond körönként átlagosan és a játék
folyamán összesen hány mezőt haladt előre! Az átlagértéket két tizedesjegy
pontossággal adja meg!
"""

print(f"A játékos átlagosan {sum(tarolt_dobasok) / dobasok_szama:2f} mezőt, összesen {sum(tarolt_dobasok)} mezőt haladt előre.")

print("\n4.Feladat")
"""
4. A mintának megfelelően adja meg, hogy Botond hány alkalommal dobott hatost! Ha
egyszer sem, akkor a “A játékos sajnos egy alkalommal sem dobott hatost.” szöveg
kerüljön megjelenítésre!
"""
szamlalo = 0
for szam in tarolt_dobasok:
    if szam == 6:
        szamlalo += 1

if szamlalo > 0:
    print(f"Botond {szamlalo} alkalommal dobott hatost!")
else:
    print("A játékos sajnos egy alkalommal sem dobott hatost.")

print("\n5.Feladat")
paros = 0

for i in tarolt_dobasok:
    if i % 2 == 0:
        paros += 1

if paros > 0:
    print(f'A játékos {paros} alkalommal dobott páros számot.')
else:
    print("A játékos egy alkalommal sem dobott páros számot!")


print("\n6.Feladat")
"""
A játékos 3 alkalommal dobott kevesebbet, mint előző körben.
"""
kevesebb = 0
for dobas in range(dobasok_szama -1):
    if tarolt_dobasok[dobas] < tarolt_dobasok[dobas+1]:
        kevesebb += 1
print("A játékos "+str(kevesebb)+" alkalommal dobott kevesebbet, mint előző körben.")
