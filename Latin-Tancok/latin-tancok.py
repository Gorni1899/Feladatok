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