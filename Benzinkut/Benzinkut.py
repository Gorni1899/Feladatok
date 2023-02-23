"""
Benzinkút
Írjon egy programot, amely egy benzinkút napi üzemanyag-eladását rögzíti! A benzinkúton
két fajta üzemanyagot árulnak: benzint (B) és dieselt (D). Az egy alkalommal eladott
üzemanyag mennyisége 1-200 literig terjedhet. Amennyiben a felhasználó által megadott
üzemanyag mennyiségnél 0l szerepel, az ne számítson vásárlásnak, és ne kerüljön
rögzítésre!

Például:
20l benzin rögzítése: B20
5l benzin rögzítése: B5
43l diesel rögzítése: D43
"""
print("1.Feladat")
"""
1. A mintának megfelelően olvassa be és rögzítse az üzemanyag-eladásokat! Az
adatbekérés mindaddig folytatódjon, amíg a felhasználó csupán ENTER-t nem üt!
"""

tarolt_tankolasok = []
tankolas = input("Adja meg az üzemanyag típusát és mennyiségét! (pl. B4 vagy D23) ")

while tankolas != "":
        tarolt_tankolasok.append(tankolas)
        tankolas = input("Adja meg az üzemanyag típusát és mennyiségét! (pl. B4 vagy D23) ")

print("\n2.Feladat")
# Adja meg a tankolások számát!
print(f"A benzinkúton {len(tarolt_tankolasok)} alkalommal vásároltak.")

print("\n3.Feladat")
# 3. Adja meg, hogy hány liter benzint vásároltak összesen!
ossz_tankolas = 0

for tankolas in tarolt_tankolasok:
        ossz_tankolas += int(tankolas[1:])
print(f'{ossz_tankolas}l benzint adtak el összesen.')

print("\n4.Feladat")
# Írja ki az egy alkalommal vásárolt átlagos
# üzemanyag-mennyiséget két tizedesjegyre kerekítve!

print(f'Egy alkalommal átlagosan {ossz_tankolas / len(tarolt_tankolasok)}l üzemanyagot vásároltak.')

print('\n5.Feladat')
# Adja meg, hogy mennyi volt az egy alkalommal vásárolt legnagyobb dieselmennyiség!
max_diesel = 0
diesel = []
for tankolas in tarolt_tankolasok:
        if tankolas[0] == 'D':
                diesel.append(int(tankolas[1:]))

for maximum in diesel:
        if max_diesel < maximum:
                max_diesel = maximum

print(f'Az egy alkalommal eladott legnagyobb diesel mennyiség {max_diesel}l volt.')