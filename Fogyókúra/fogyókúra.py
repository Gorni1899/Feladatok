print("1.Feladat")

"""
1. Olvassa be a mintának megfelelően, és tárolja el, hogy hány héten át tartott a fogyókúra, és
Mari néni milyen célt tűzött ki maga elé!
"""
tarolt_sulyok = []

hetek_szama = int(input("Hetek száma: "))

cel = float(input("Elérni kívánt testtömeg (kg)= "))

print("\n2.Feladat")

for het in range(1, hetek_szama +1):
    aktualis_suly = float(input(f"{het}. héten az aktuális súly: "))
    tarolt_sulyok.append(aktualis_suly)

print("\n3.Feladat")
siker = 0
for index, statisztika in enumerate(tarolt_sulyok, start=1):
    if statisztika < cel:
        siker += 1
        print(f'Marinéni a {index}. héten érte el a célt.')
        break

if siker == 0:
    print("Sajnos Mari néni nem érte el a célját.")

print("\n4.Feladat")

szamlalo = 0

for index in range(hetek_szama -1):
    if tarolt_sulyok[index] < tarolt_sulyok[index+1]:
        szamlalo += 1

print(f"A tömege {szamlalo} esetben nőtt egyik hétről a másikra.")