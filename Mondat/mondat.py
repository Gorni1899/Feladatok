print("1.Feladat")

mintamondat = "Melyik a leghosszabb szó? "#input("Add meg a mondatot: ")

print("\n2.Feladat")

kiszurendo_karakterek = " ,.?!;"
betuk = 0
for betu in mintamondat:
    if betu not in kiszurendo_karakterek:
        betuk += 1

print(f'A mondatban előforduló betűk száma: {betuk}.')

print("\n3.Feladat")
szavak = 0

for szo in mintamondat.split():
    szavak += 1

print("A szavak száma "+ str(szavak)+".")

print("\n4.Feladat")

mgh_db = 0
mgh = "aáeéiíoóöőüű"

for m in mintamondat:
    if m in mgh:
        mgh_db += 1
print("A mondatban előforduló magánhangzók száma:",mgh_db)

print("\n5.Feladat")
# A leghosszabb szó a(z) leghosszabb 11 betűből áll.
max_hossza = ""
for hossz in mintamondat.split():
    if len(max_hossza) < len(hossz):
        max_hossza = hossz

print(f"A leghosszabb szó a(z) {max_hossza}  {len(max_hossza)} betűből áll.")

print("\n6.Feladat")
bekert_szo = input("Add meg a keresett szót: ")

if bekert_szo in mintamondat:
    print("Van a mondatban ilyen szó!")
else:
    print("A keresett szó nem fordul elő a mondatban.")