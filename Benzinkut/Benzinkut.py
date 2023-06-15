"""
Benzinkút
Írjon egy programot, amely egy benzinkút napi üzemanyag-eladását rögzíti! A benzinkúton
két fajta üzemanyagot árulnak: benzint (B) és dieselt (D). Az egy alkalommal eladott
üzemanyag mennyisége 1-200 literig terjedhet. Amennyiben a felhasználó által megadott
üzemanyag mennyiségnél 0l szerepel, az ne számítson vásárlásnak, és ne kerüljön
rögzítésre.

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
diesel_tarolas = []
tarolt_tankolasok = []
tankolas = input("Adja meg az üzemanyag típusát és mennyiségét! (pl. B4 vagy D23) ")
max_tankolas = 201
while tankolas != "" and int(tankolas[1:]) < max_tankolas:
        if tankolas[0] == "D" and tankolas[1:] != "0":
                diesel_tarolas.append(int(tankolas[1:]))
        if tankolas[1:] != "0":
                tarolt_tankolasok.append(int(tankolas[1:]))
        tankolas = input("Adja meg az üzemanyag típusát és mennyiségét! (pl. B4 vagy D23) ")

print("\n2.Feladat")
# Adja meg a tankolások számát!
print(f"A benzinkúton {len(tarolt_tankolasok)} alkalommal vásároltak.")

print("\n3.Feladat")
# 3. Adja meg, hogy hány liter benzint vásároltak összesen!

print(f"{sum(tarolt_tankolasok)}l benzint adtak el összesen.")

print("\n4.Feladat")
# Írja ki az egy alkalommal vásárolt átlagos
# üzemanyag-mennyiséget két tizedesjegyre kerekítve!

print(f'Egy alkalommal átlagosan {sum(tarolt_tankolasok) / len(tarolt_tankolasok):.2f}l üzemanyagot vásároltak.')

print('\n5.Feladat')
# Adja meg, hogy mennyi volt az egy alkalommal vásárolt legnagyobb dieselmennyiség!
max_diesel = 0

for tankolas in diesel_tarolas:
        if max_diesel < tankolas:
                max_diesel = tankolas

print(f'Az egy alkalommal eladott legnagyobb diesel mennyiség {max_diesel}l volt.')