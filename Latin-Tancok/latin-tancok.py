print("1.Feladat")
"""
Egy nagy listában fogom tárolni az adatokat aminek az egyes táncra vonatkozó elemei szótárak lesznek.
"""
adatok = []
tanc = {}
tancok = []

with open("tancrend.txt", "r", encoding="utf-8") as file:
    for sor in file:
        adatok.append(sor.strip())
        if len(adatok) == 3:
            tanc["nev"] = adatok[0]
            tanc["lany"] = adatok[1]
            tanc["fiu"] = adatok[2]
            tancok.append(tanc)
            adatok = []
            tanc = {}

print(tancok)


print("\n2.Feladat")
"""
Két print utasítást fogok használni és f sztringet
"""
#2. Írassa ki a képernyőre, hogy melyik volt az elsőként és melyik az utolsóként bemutatott tánc neve!
print(f"Az elsőként bemutatott tánc neve a {tancok[0]['nev']} volt.")
print(f"Az utolsóként bemutatott tánc neve a {tancok[-1]['nev']} volt.")

print("\n3.Feladat")
"""
Megszámlálós algoritmust használok.
"""
# 3. Hány pár mutatta be a sambát? A választ jelenítse meg a képernyőn!

szamlalo = 0
for tanc in tancok:
    if tanc["nev"] == "samba":
        szamlalo += 1
print("A szambát "+str(szamlalo)+" pár mutatta be.")

print("\n4.Feladat")
"""

"""
# 4. Írassa ki a képernyőre, hogy Vilma mely táncokban szerepelt!
print("Vilma az alábbi táncokban szerepelt: ")
for tanc in tancok:
    if tanc['lany'] == "Vilma":
        print(tanc['nev'])

print("\n5.Feladat")
"""

"""
# Kérje be egy tánc nevét, majd írassa ki a képernyőre, hogy az adott táncot Vilma kivel
# mutatta be! Például ha a bekért tánc a samba, és Vilma párja Bertalan volt, akkor
# „A samba bemutatóján Vilma párja Bertalan volt.” szöveg jelenjen meg!
# Ha Vilma az adott tánc bemutatóján nem szerepelt, akkor azt írja ki a képernyőre, hogy
# „Vilma nem táncolt samba-t.”.
bekert_tanc = input("Adja meg a tánc nevét: ")
szamlalo = 0
for tanc in tancok:
    if tanc['nev'] == bekert_tanc and tanc['lany'] == "Vilma":
        print(f'A {bekert_tanc} bemutatóján Vilma párja {tanc["fiu"]} volt.')
        szamlalo += 1

if szamlalo == 0:
    print(f"Vilma nem táncolt {bekert_tanc}-t.")

print("\n6.Feladat")
"""
Ennél a feladatnál halmazba fogom tölteni az adatokat, hogy a duplikációt elkerüljem.
A join metódus segítségével fogom megvalósítani az elemek közötti vesszőket.
"""
#6. Készítsen listát a bemutatón részt vett fiúkról és lányokról! A listát a szereplok.txt
#nevű szöveges állományba mentse el a következő formátumban: a neveket vesszők
#válasszák el egymástól, de az utolsó név után már ne szerepeljen írásjel. P

with open("szereplok.txt", 'w', encoding='utf-8') as szereplok:
    fiuk = set()
    lanyok = set()
    for tanc in tancok:
        fiuk.add(tanc['fiu'])
        lanyok.add(tanc['lany'])
    elvalaszto_karakter = ", "

    print("Fiúk: ", elvalaszto_karakter.join(fiuk), file=szereplok)
    print("Lányok: ", elvalaszto_karakter.join(lanyok), file=szereplok)

print("\n7.Feladat")
"""
Szótárt hozunk létre aminek az elemei a meglévő listánknak a fiú és lány elemei amiket beletöltünk.
Amennyiben nem szerepel még az adott név a feltöltendő szótárunkba akkor 1 értéket adunk neki.
Amennyiben már szerepel benne akkor a hozzárendelt értéket 1-el növeljük.
Majd futtatunk egy max kereső algoritmust és megkapjuk a legtöbbet szerepelt, lányt és fiút.

"""
# Írja ki a képernyőre, hogy melyik fiú szerepelt a legtöbbször a fiúk közül, és melyik lány
# a lányok közül! Ha több fiú, vagy több lány is megfelel a feltételeknek, akkor valamennyi
# fiú, illetve valamennyi lány nevét írja ki.
fiuk = {}
lanyok = {}

for tanc in tancok:
    if tanc['fiu'] not in fiuk:
        fiuk[tanc['fiu']] = 1
    else:
        fiuk[tanc['fiu']] += 1

    if tanc['lany'] not in lanyok:
        lanyok[tanc['lany']] = 1
    else:
        lanyok[tanc['lany']] += 1
# Az első fázisunkkal megvagyunk.

# Itt algoritmus max érték keresést fogunk alkalmazni.
max_fiu = 0
for x in fiuk:
    if fiuk[x] > max_fiu:
        max_fiu = fiuk[x]

print("A legtöbbet táncolt fiú(k):")
for y in fiuk:
    if fiuk[y] == max_fiu:
        print(y)

max_lanyok = 0

for lany in lanyok:
    if lanyok[lany] > max_lanyok:
        max_lanyok = lanyok[lany]
print("\nA legtöbbet táncolt lány(ok):")
for lany in lanyok:
    if lanyok[lany] == max_lanyok:
        print(lany)