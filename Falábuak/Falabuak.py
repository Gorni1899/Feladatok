
print("1.Feladat")

fordulok_szama = int(input("Fordulók száma: "))

print("\n2.Feladat")
tarolt_eredmenyek = []
for fordulo in range(1, fordulok_szama +1):
    aktualis_eredmeny = int(input(f"{fordulo}. fordulóban a gólkülönbség: "))
    tarolt_eredmenyek.append(aktualis_eredmeny)

print(tarolt_eredmenyek)

print("\n3.Feladat")
gyozelem = 0
dontetlen = 0
vereseg = 0

for i in tarolt_eredmenyek:
    if i > 0:
        gyozelem += 1
    elif i < 0:
        vereseg += 1
    else:
        dontetlen += 1

print(f"A szezonban a csapatnak {gyozelem} győzelme, {vereseg} veresége, {dontetlen} döntetlene volt.")

print("\n4.Feladat")
print(f"A csapatnak a szezonban összesen {gyozelem * 3 + dontetlen} pontja lett.")

print("\n5.Feladat")
if gyozelem > vereseg + dontetlen:
    print("A csapatnak több győztes mérkőzése volt, mint veresége és döntelene együttvéve.")

print("\n6.Feladat")
cel = 0
for index in range(fordulok_szama -1):
    if tarolt_eredmenyek[index] > 0 and tarolt_eredmenyek[index] < tarolt_eredmenyek[index+1]:
        cel += 1

print(f"A kitűzött célt {cel} alkalommal sikerült elérnie a csapatnak.")