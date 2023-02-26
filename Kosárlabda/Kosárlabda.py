"""
Készítsen egy programot, amely rögzíti és kiértékeli egy kosárcsapatnak a szeonban elért
eredményeit!
"""
print("1.Feladat")
"""
1. Olvassa be a kosárcsapat heti fordulókban elért
eredményeit! A heti fordulók eredményeit egy karaktersorozat formájában adja meg!
(pl: 11x21xx221) xxx112x1xx111
"""
eredmenyek = input("Adja meg a kosárlabdacsapat eredményét! ")

print("\n2.Feladat")
"""
2. A program a minta szerint írja ki a képernyőre a fordulók és a vereségek számát!
"""
vereseg = 0

for eredmeny in eredmenyek:
    if eredmeny == '2':
        vereseg += 1

print(f"A fordulok száma {len(eredmenyek)}. \nA vereségek száma "+str(vereseg)+" volt.")

print("\n3.Feladat")
pontszamok = 0

for pontok in eredmenyek:
    if pontok == '1':
        pontszamok += 3
    elif pontok == 'x':
        pontszamok += 1

print(f'A fordulók során szerzett összpontszám: {pontszamok}')

print("\n4.Feladat")
"""
Hány fordulón keresztül tartott a leghosszabb győzelmi széria, melyben a csapat
megszakítás nélkül legyőzte ellenfelét? A mintának megfelelően adja meg az
eredményt!
"""
gyozelmi_szeria = 0

for index in range(len(eredmenyek)-1):
    if eredmenyek[index] == '1' and eredmenyek[index+1] == '1':
        gyozelmi_szeria += 1

if gyozelmi_szeria > 0:
    print(f"A leghosszabb győzelmi széria {gyozelmi_szeria +1} fordulón át tartott.")

print("\n5.Feladat")
"""
5. Előfordult-e a szezonban olyan sorozat, amikor vereséget, döntetlen, majd győzelem
követett közvetlenül? Ha igen, milyen eredmény követette ezt a hármas sorozatot?
(Feltételezheti hogy a szezonban legfeljebb csak egy ilyen sorozat volt.) A választ a
minta szerint jelenítse meg!
"""
for index in range(len(eredmenyek)-1):
    if eredmenyek[index] == '2' and eredmenyek[index+1] == 'x' and eredmenyek[index+2] == '1':
        print("Volt vereség-döntetlen-győzelem hármas a szezonban.")
        if eredmenyek[index+3] == '2':
            print("Ezután vereség következett.")
        elif eredmenyek[index+3] == 'x':
            print("Ezután döntetlen következett.")
        elif eredmenyek[index+3] == '1':
            print("Ezután gyözelem következett.")
        else:
            print('Ezután nem volt több mérkőzés.')