"""
Készítsen egy programot, amely rögzíti és kiértékeli egy kosárcsapatnak a szeonban elért
eredményeit!
A program forráskódját mentse “kosarlabda” néven! A program megírásakor a felhasználó
által megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti,
hogy a rendelkezésre álló adatok a leírtaknak megfelelnek
"""

"""
1. Olvassa be a mintának megfelelően a kosárcsapat heti fordulókban elért
eredményeit!
"""
tarolt_eredmenyek = []
elert_eredmenyek = 'xxx112x1xx111'#input("Adja meg a kosárlabdacsapat eredményét! ")

for eredmeny in elert_eredmenyek:
    tarolt_eredmenyek.append(eredmeny)
# 2. A program a minta szerint írja ki a képernyőre a fordulók és a vereségek számát!

vereseg = 0
for eredmeny in elert_eredmenyek:
    if eredmeny == '2':
        vereseg += 1

print(f"A fordulók száma {len(elert_eredmenyek)}")
print("A vereségel száma",vereseg)
"""
3. A mintában megadott módon jelenítse meg a fordulók során elért összpontszámot! A
győzelem 3, a döntetlen 1, a vereség 0 pontot ér.
"""

gyozelem = 0
dontetlen = 0

for eredmeny in elert_eredmenyek:
    if eredmeny == '1':
        gyozelem += 3
    elif eredmeny == "0":
        dontetlen += 1

print(f"A fordulók során szerzett összpontszám: {gyozelem + dontetlen}")

"""
4. Hány fordulón keresztül tartott a leghosszabb győzelmi széria, melyben a csapat
megszakítás nélkül legyőzte ellenfelét? A mintának megfelelően adja meg az
eredményt!
"""
gyozelmi_szeria = 0

for index in range(len(tarolt_eredmenyek)-1):
    if tarolt_eredmenyek[index] == "1" and tarolt_eredmenyek[index+1] == '1':
        gyozelmi_szeria += 1

print(f'A leghosszabb győzelmi széria {gyozelmi_szeria} fordulón át tartott.')

"""
5.feladat
Volt vereség-döntetlen-győzelem hármas a szezonban.
Ezután döntetlen következett.
"""
v = "2"
d = "0"
gy = "1"
volt_ilyen = False
for eredmeny in range(len(tarolt_eredmenyek)-1):
    if tarolt_eredmenyek[eredmeny] == "2" and tarolt_eredmenyek[eredmeny+1] == "x" and tarolt_eredmenyek[eredmeny+2] == "1":
        print("Volt vereség-döntetlen-győzelem hármas a szezonban.")
        volt_ilyen = True

        if volt_ilyen:

            if tarolt_eredmenyek[eredmeny+3] == "2":
                print("Ezután vereség következett.")
                break
            elif tarolt_eredmenyek[eredmeny+3] == 'x':
                print("Ezután döntetlen következett.")
            elif tarolt_eredmenyek[eredmeny+3] == '1':
                print("Ezután győzelem következett.")
            else:
                print("Ezután nem volt több mérkőzés.")
